import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
num = [list(map(int, input().split())) for _ in range(t)]
prime = [False for _ in range(10000)]

def findPrime():
    for i in range(10000):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime[i] = True # 소수이면 True

def bfs():
    q = deque()
    q.append((start, 0))

    visited = [0 for _ in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)

        if now == end:
            return cnt

        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[tmp] == 0 and prime[tmp] and tmp >= 1000:
                    visited[tmp] = 1
                    q.append([tmp, cnt + 1])

findPrime()
for i in range(t):
    start, end = num[i][0], num[i][1]
    result = bfs()
    if result == None:
        print("Impossible")
    else:
        print(result)