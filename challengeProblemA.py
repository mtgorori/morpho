import sys

def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

def main():
  #input N
  print('input N in the range 0<=N<=30')
  N = sys.stdin.readline()
  list = [i for i in range(N)]
  # for文で全要素を表示
  for i in range(len(list)):  # lenでリストの要素数を求める, rangeにループ回数(回数分の要素のリストが戻り値), inはリストをとる
    print '%d, ' % (list[i]), # print文の末尾に「,」を付けると改行しない
    print '\n'


if __name__ == "__main__":
  main()
