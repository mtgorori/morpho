import sys
import cProfile
import pstats
from memory_profiler import profile
import numpy as np
from numba import jit

@profile
@jit
def cnt3():
    digits = '0123'
    cnt = 0
    tmp = 0
    #input N
    #print('input N in the range 0<=N<=30')
    N = int(input())
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
            cnt += ''.join(reversed(res or '0')).count('3')
    print(cnt)

if __name__ == "__main__":
  cProfile.run('cnt3()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
