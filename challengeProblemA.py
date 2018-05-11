import sys
import cProfile
import pstats
from memory_profiler import profile
<<<<<<< HEAD
<<<<<<< HEAD
from numba import jit
from functools import reduce
=======
import  numpy as np
>>>>>>> parent of 36ff1c6... 初期化等細かい調整
=======
import  numpy as np
>>>>>>> parent of 36ff1c6... 初期化等細かい調整

def NsinFrom10sin(X, n):
    if (int(X/n)):
        return NsinFrom10sin(int(X/n), n)+ str(X%n)
    return str(X%n)

<<<<<<< HEAD
<<<<<<< HEAD
=======
@profile
>>>>>>> parent of 36ff1c6... 初期化等細かい調整
=======
@profile
>>>>>>> parent of 36ff1c6... 初期化等細かい調整
def main():
  cnt = 0
  #input N
  #print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
  #list01 = range(1,N)
      list01 = [ list(str(NsinFrom10sin(x,4))) for x in range(1,int(N/2)+1) ]
      list01 = reduce(lambda x, y: x + y, list01)
      list02 = [ list(str(NsinFrom10sin(x,4))) for x in range(int(N/2)+1,N+1) ]
      list02 = reduce(lambda x, y: x + y, list02)
      print(list01)
      print(list02)
      print(list01.count('3')+list02.count('3'))

if __name__ == "__main__":
<<<<<<< HEAD
<<<<<<< HEAD
    main()
=======
  cProfile.run('main()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
>>>>>>> parent of 36ff1c6... 初期化等細かい調整
=======
  cProfile.run('main()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
>>>>>>> parent of 36ff1c6... 初期化等細かい調整
