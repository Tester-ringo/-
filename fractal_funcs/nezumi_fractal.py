
#nezumi_fractal

"""
送ってくれたサイトを参考に野澤が実装した階乗計算関数
"""

import math

def fractal(n: int) -> int:
    """送ってくれたサイトを参考に野澤が実装した階乗計算関数
    """
    if not isinstance(n, int):
        raise ValueError("fractal(n)の引数はintのみを受け付けます")
    elif n < 0:
        raise ValueError("fractal(n)は正の値を指定してください")
    elif n <= 20:
        results = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
                   39916800, 479001600, 6227020800, 87178291200, 1307674368000,
                   20922789888000, 355687428096000, 6402373705728000,
                   121645100408832000, 2432902008176640000)
        return results[n]
    #ここからが本番
    def simple_double_fraltal(a, b):
        """aからbまでの2重階乗を計算します""" #simple_double_fraltal(3, 8) -> 3*5*7
        result_value = 1
        for i in range(a, b, 2):
            result_value *= i
        return result_value
    m = n.bit_length() - 1
    two_count = n - n.bit_count() #n!に含まれる2の数 
    dupe_point = [math.floor(n/2**i) + 1 | 1 for i in range(m)] #奇数の総積の重複地点を列挙（説明下手）
    result_value = 1 #returnする値。ここに重複地点で分けた区間を大きい順に掛けていく。
                     #ただ単純に順番に掛けているため、ボトルネックとなる。理想は2分探索のように掛けていく事。
                     #しかしその場合、コードの可読性がさらに下がるため、見送った。
    for i in range(m-1): #奇数の総積の重複地点で区切った区間の数だけ繰り返す
        little_point_value = dupe_point[i+1] #今見ている重複区間の小さい値
        big_point_value = dupe_point[i] #今見ている重複区間の大きい値
        fractal_part = simple_double_fraltal(little_point_value, big_point_value) #区間の総積
        duped_fractal_part = fractal_part ** (i+1) #今見ている区間を重分だけ掛ける。
                                                   #ただの累乗を使用しているためボトルネックになる可能性あり。
        result_value *= duped_fractal_part #返り値に掛ける
    result_value <<= two_count #n!に含まれている2の個数分だけビットシフトする。
                               #これは、2^(ビットシフトした分)を掛けていることと同値である。
    return result_value




