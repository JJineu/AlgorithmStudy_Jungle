import sys
input = sys.stdin.readline

N = int(input()) #72
M = 2 # 소수 2부터 시작

while N != 1:  # N과 M을 나눴을때 몫이 1이 되면 멈춤.
  if N % M == 0:
    print(M)
    N = N//M
  else:
    M += 1