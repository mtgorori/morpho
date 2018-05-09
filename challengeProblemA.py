import sys
import cProfile
import pstats
from memory_profiler import profile
from numba import jit


from functools import reduce
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
  print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
  #list01 = range(1,N)
      list01 = [ list(str(NsinFrom10sin(x,4))) for x in range(1,N) ]
      print(list01)
      list01 = reduce(lambda x, y: x + y, list01)
      print(list01.count('3'))

if __name__ == "__main__":
    main()
