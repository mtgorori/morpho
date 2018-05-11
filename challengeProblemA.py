import numba
import numpy as np

@numba.jit
def main():
  cnt = 0
  tmp = 0
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      list01 = []
      for x in range(1,N+1):
          list01.append(np.base_repr(x,4))
      for i in list01:
          tmp = i.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
    main()
