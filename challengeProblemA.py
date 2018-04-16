def NsinFrom10sin(X, n):
    if (int(X/n)):
        return NsinFrom10sin(int(X/n), n)+str(X%n)
    return str(X%n)

def main():
  cnt = 0
  #input N
  #print('input N in the range 0<=N<=30')
  N = int(input())
  if N>30:
      pass
  else:
      N = 4**N
      list01 = [ NsinFrom10sin(x,4) for x in range(1,N+1) ]
      #print(list01)
      #print(type(len(list01)))
      for i in list01:
          tmp = i.count('3')
          cnt += tmp
      print(cnt)

if __name__ == "__main__":
  main()
