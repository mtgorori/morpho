import sys
import cProfile
import pstats
from memory_profiler import profile
import numpy as np
from numba import jit, i8

@profile
@jit('i8(i8)')
def cnt3(N):
    digits = '0123'
    cnt = 0
    tmp = 0
    if N>30:
        pass
    else:
        N = 4**N
        #change to xrange if python2x
        for i in range(1,N+1):
            num = i
            res = []
            while num:
                res.append(digits[num % 4])
                num //= 4
            cnt += ''.join(reversed(res)).count('3')
    return cnt

if __name__ == "__main__":
    N = int(input())
    cnt = cnt3(N)
    print(cnt)
