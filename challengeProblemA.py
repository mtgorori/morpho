import numba

def memoize(f): #メモ化関数
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

@memoize
def FoursinFrom10sin(X):
    if (int(X/4)):
        return FoursinFrom10sin(int(X/4))+ str(X%4)
    return str(X%4)

@numba.jit
def count():
  cnt = 0
  tmp = 0
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      list01 = []
      for x in range(1,N+1):
          list01.append(FoursinFrom10sin(x))
      for i in list01:
          tmp = i.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
    count()
