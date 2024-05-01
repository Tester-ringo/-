
#copy_and_paste_fractal

"""
送ってくれたサイトのアルゴリズムをコピペ
"""

def F(L: int, U: int) -> int:
    """
    L, U: 奇数
    [L, U) の奇数の総積を分割統治法で計算する。
    """
    if L >= U: return 1

    max_bits = (U - 2).bit_length()  # 掛けられる最大の奇数のビット長
    num_operands = (U - L) // 2  # 掛けられる奇数の個数

    # [L, U) の奇数の総積のビット長は　max_bits * num_operands を超えない
    # これが long に収まれば多倍長演算を回避して計算できる
    if max_bits * num_operands < 63:  # 63 = sys.maxsize.bit_length()
        total = L
        for i in range(L + 2, U, 2):
            total *= i
        return total

    # 多倍長演算を回避するために分割して計算する
    mid = (L + num_operands) | 1
    left = F(L, mid)
    right = F(mid, U)

    return left * right

def calc_odd_part(n: int) -> int:
    """
    n! を (奇数) * (2の冪乗) と表したときの (奇数) の部分を計算する
    """

    result = 1
    L_i = 3
    tmp = 1  # F(3, U_i)
    m = n.bit_length() - 1  # n // (2 ** m) > 0 となる最大の整数

    for i in range(m - 1, -1, -1):
        # U_i は n//(2**i) より大きい最小の奇数
        U_i = ((n >> i) + 1) | 1

        # [1, U_i)　のうち、[1, L_i) は計算済みなので再利用し [L_i, U_i) のみ計算する
        tmp *= F(L_i, U_i)

        # 計算済みの範囲を更新 (L_{i} <- U_{i + 1})
        L_i = U_i

        result *= tmp

    return result


SmallFactorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
                   39916800, 479001600, 6227020800, 87178291200, 1307674368000,
                   20922789888000, 355687428096000, 6402373705728000,
                   121645100408832000, 2432902008176640000]


def factorial(n: int) -> int:
    """送ってくれたサイトの階乗計算のアルゴリズムをそのままコピペしました。
    """
    # n が小さい場合は埋め込んだ結果を使う
    if n <= 20: return SmallFactorials[n]

    # n! = odd_part * (2 ** two_exponent) と表せる
    odd_part = calc_odd_part(n)
    two_exponent = n - bin(n).count('1')  # n - popcount(n)

    return odd_part << two_exponent


