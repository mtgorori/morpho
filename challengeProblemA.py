import numpy as np
from numba import jit

@jit('i8(i8)')
def cnt3(N):
    digits = '0123'
    cnt = 0
    tmp = 0
    a = 0
    if N>30:
        pass
    else:
        N = 4**N
        #change to xrange if python2x
        for i in range(1,N+1):
            num = i
            while num:
                a = num % 4
                if a == 3:
                    cnt += 1
                num //= 4
    return cnt

if __name__ == "__main__":
    N = int(input())
    cnt = cnt3(N)
    print(cnt)
