
#simple_fractal

"""
簡易実装の階乗計算関数
"""

import math

def fracltal(n: int) -> int:
    """for文を用いた簡易階乗計算関数
    """
    if not isinstance(n, int):
        raise ValueError("fractal(n)の引数はintのみを受け付けます")
    elif n < 0:
        raise ValueError("fractal(n)は正の値を指定してください")
    result_value = 1
    for i in range(2, n+1):
        result_value *= i
    return result_value





