import sys

def NsinFrom10sin(X, n):
    if (int(X/n)):
        return NsinFrom10sin(int(X/n), n)+str(X%n)
    return str(X%n)

def main():
  #input N
  print('input N in the range 0<=N<=30')
  N = int(input())
  N = 4**N
  list01 = range(1,N)
  list01 = [ int(NsinFrom10sin(x,4)) for x in list01 ]
  print(list01)
  print(N)

if __name__ == "__main__":
  main()
