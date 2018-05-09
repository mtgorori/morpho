import sys
import cProfile
import pstats
from memory_profiler import profile

def NsinFrom10sin(X, n):
    if (int(X/n)):
        return NsinFrom10sin(int(X/n), n)+str(X%n)
    return str(X%n)

@profile
def main():
  cnt = 0
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
      print(sys.getsizeof(list01))

if __name__ == "__main__":
  cProfile.run('main()', filename = 'main.prof')
  sts = pstats.Stats('main.prof')
  sts.strip_dirs().sort_stats('cumulative').print_stats()
