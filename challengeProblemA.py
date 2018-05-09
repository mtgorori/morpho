import sys
import cProfile
import pstats
from memory_profiler import profile
from numba import jit

@jit
def NsinFrom10sin(X, n):
    if (int(X/n)):
        return NsinFrom10sin(int(X/n), n)+ str(X%n)
    return str(X%n)

@jit
def main():
  cnt = 0
  tmp = 0
  #input N
  #print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      for i in range(1,N+1):
          x = NsinFrom10sin(i, 4)
          tmp = x.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
    main()
 # cProfile.run('main()', filename = 'main.prof')
  #sts = pstats.Stats('main.prof')
  #sts.strip_dirs().sort_stats('cumulative').print_stats()
