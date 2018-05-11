<<<<<<< HEAD
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
=======
import sys
import cProfile
import pstats
from memory_profiler import profile
import numpy as np
from numba import jit

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base_repr(number, base=2, padding=0):
    """
    Return a string representation of a number in the given base system.
    Parameters
    ----------
    number : int
        The value to convert. Only positive values are handled.
    base : int, optional
        Convert `number` to the `base` number system. The valid range is 2-36,
        the default value is 2.
    padding : int, optional
        Number of zeros padded on the left. Default is 0 (no padding).
    Returns
    -------
    out : str
        String representation of `number` in `base` system.
    See Also
    --------
    binary_repr : Faster version of `base_repr` for base 2.
    Examples
    --------
    >>> np.base_repr(5)
    '101'
    >>> np.base_repr(6, 5)
    '11'
    >>> np.base_repr(7, base=5, padding=3)
    '00012'
    >>> np.base_repr(10, base=16)
    'A'
    >>> np.base_repr(32, base=16)
    '20'
    """
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
>>>>>>> a56ccb94c4228603376228e8e355eec6cd763d5b
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
<<<<<<< HEAD
      list01 = []
      for x in range(1,N+1):
          list01.append(FoursinFrom10sin(x))
      for i in list01:
          tmp = i.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
    count()
>>>>>>> parent of 054b599... 基数変換関数を導入した
=======
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
>>>>>>> a56ccb94c4228603376228e8e355eec6cd763d5b
