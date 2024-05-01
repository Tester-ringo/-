
#old_nezumi_fractal

"""
以前野澤が作成した階乗計算関数
"""

import math

import sys
import math
import time
import itertools
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(500_000) #エラーが出たらもっと増やそう！

NUMBER_OF_CORE = multiprocessing.cpu_count()

def _select_base(f): #この関数はネットのコピペ
    def wrap(n) -> bool:
        if n < 2047:
            bases = (2,)
        elif n < 1373653:
            bases = (2, 3)
        elif n < 9080191:
            bases = (31, 73)
        elif n < 25326001:
            bases = (2, 3, 5)
        elif n < 3215031751:
            bases = (2, 3, 5, 7)
        elif n < 350269456337:
            bases = (4230279247111683200, 14694767155120705706,
                     16641139526367750375)
        elif n < 55245642489451:
            bases = (2, 141889084524735,
                     1199124725622454117, 11096072698276303650)
        elif n < 7999252175582851:
            bases = (2, 4130806001517,
                     149795463772692060, 186635894390467037,
                     3967304179347715805)
        elif n < 585226005592931977:
            bases = (2, 123635709730000,
                     9233062284813009, 43835965440333360,
                     761179012939631437, 1263739024124850375)
        elif n < (2<<63):
            bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
        elif n < 3317044064679887385961981:
            bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
        else:
            raise OverflowError
        return f(n, bases)
    return wrap

@_select_base
def is_prime(n: int, mr_bases: tuple) -> bool: #この関数はネットのコピペ
    if n < 2:
        return False
    elif n == 2:
        return True
    elif not n&1:
        return False
    d = n - 1
    s = 0
    while not d & 1: #d & 1 == 0
        s += 1 
        d >>= 1
    for a in mr_bases:
        if a == n:
            return False
        a %= n
        x = pow(a, d, n) # a^d mod n
        if x == 1 or x == n-1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == n-1: # a^(d*2^r) mod n
                break
        else: 
            return False
    return True

def _multiply_list(number_list, measure_time=True):
        start_time = time.time()
        while len(number_list)>1 and (not measure_time or time.time()-start_time<1):
            multiplyed = [i*j for i, j in zip(number_list[::2], number_list[1::2])] #2分掛け合わせ。（いい名前を思いつかなかった。
            if len(number_list)&1:
                multiplyed.append(number_list[-1])
            number_list = multiplyed
        return number_list

def _prime_extract(x):
    return [i for i in x if is_prime(i)]

def fractal(x:int) -> int:
    """以前野澤が作成した階乗計算関数
    """
    if x < 2:
        return 1
    split_times = math.ceil(x/200000)
    split_times = NUMBER_OF_CORE if split_times > NUMBER_OF_CORE else split_times
    if split_times == 1:
        prime_list = [i for i in range(x+1) if is_prime(i)]
    else:
        with ProcessPoolExecutor(max_workers=split_times) as executor:
            results = executor.map(_prime_extract, [range(int((x+1)/NUMBER_OF_CORE*i), int((x+1)/NUMBER_OF_CORE*(i+1))) for i in range(NUMBER_OF_CORE)])
            prime_list = list(itertools.chain.from_iterable(list(results)))
    number_of_included_func = lambda base: sum(x//base**power for power in range(1, int(math.log(x)/math.log(base))+1)) #素数(base)がxの中に何個因数として含まれるかを列挙。
    number_of_included_list  = list(map(number_of_included_func, prime_list)) #列挙した素数に対して、1〜xまでに幾つ因数として含まれるかをmap
    prime_pow = [prime**count for prime, count in zip(prime_list, number_of_included_list)]
    while len(prime_pow) > 1:
        split_times = math.ceil(len(prime_pow)/3000)
        split_times = NUMBER_OF_CORE if split_times > NUMBER_OF_CORE else split_times
        if split_times == 1:
            prime_pow = _multiply_list(prime_pow, False)
            continue
        with ProcessPoolExecutor(max_workers=split_times) as executor:
            results = executor.map(_multiply_list, [prime_pow[int(len(prime_pow)/split_times*i) : int(len(prime_pow)/split_times*(i+1))] for i in range(split_times)])
            prime_pow = list(itertools.chain.from_iterable(list(results)))
    return prime_pow[0]





