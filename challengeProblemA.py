import sys
import cProfile
import pstats
from memory_profiler import profile
import numpy as np
from numba import jit

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base_repr(number, base=2, padding=0):

    num = abs(number)
    res = []
    while num:
        res.append(digits[num % base])
        num //= base
    if padding:
        res.append('0' * padding)
    if number < 0:
        res.append('-')
    return ''.join(reversed(res or '0'))

@profile
@jit
def cnt3():
  cnt = 0
  tmp = 0
  tmp1 = 0
  #input N
  #print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      #change to xrange if python2x
      for i in range(1,N+1):
          tmp1 = np.base_repr(i,4)
          tmp = tmp1.count('3')
          cnt += tmp
      return cnt

if __name__ == "__main__":
  cProfile.run('cnt3()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
