# 네자리 수 9999까지 완탐해서 소수인지 판별
# 각 자리 수마다 숫자(0~9)를 바꿔가며 소수인 수는 큐에 넣음
# 또 자릿수를 바꿔 가며 바꿔야 하는 숫자가 나올 때 판별
# 1. 큐에 넣은 숫자는 방문 처리를 함 (visited) - 카운트 중복 방지
# 2. 과정 중에는 네 자리 숫자를 유지해야 하므로 
# 바꾼 숫자가 1000이상인지 확인

import sys
from collections import deque
input = sys.stdin.readline

prime = [False for _ in range(10000)] # True:소수, False:소수가 아님

def findPrime():
    for i in range(1000, 10000):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime[i] = True # 소수이면 True

def bfs():
    q = deque()
    q.append([start, 0])

    visited = [0 for i in range(10000)] # visited 배열
    visited[start] = 1 # 처음에 들어온 것 visited 처리 반드시 해주기

    while q:
        now, cnt = q.popleft() # 가장 처음에 들어온 거 popleft로 빼주기 
        strNow = str(now)

        # 빼낸 값이 end면 cnt 리턴
        if now == end:
            return cnt # q에서 pop한 cnt를 바로 리턴해주면 됨

        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[tmp] == 0 and prime[tmp] and tmp >= 1000: 
                # 한 자리수만 변경해서 만들어준 수에 방문한 적 없고 소수이고 1000 이상인 수 일 떄
                    visited[tmp] = 1 # 방문 처리
                    q.append([tmp, cnt + 1]) # cnt + 1을 넣어줌


t = int(input())
findPrime()

for _ in range(t):
    start, end = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")