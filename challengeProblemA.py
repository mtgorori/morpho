import sys
import cProfile
import pstats
from memory_profiler import profile
import numpy as np
from numba import jit

@profile
@jit
def main():
  cnt = 0
  #input N
  #print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      #change to xrange if python2x
      for i in range(1,N+1):
          tmp = np.base_repr(i,4)
          tmp = tmp.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
  cProfile.run('main()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
