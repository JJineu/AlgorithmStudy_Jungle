import sys, math
from collections import deque

#에라토스테네스의 체
def findPrime():
    for i in range(2, 100): #제곱근까지 조사
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs():
    q = deque()
    q.append([start, 0])
    visited = [0] * (10000)
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)
        if now == end: 
            return cnt

        for i in range(4): #i 자리에
            for j in range(10):#0~9를 넣어가며 소수인지 확인
                temp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[temp] == 0 and prime[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt+1]) 
                    #어차피 cnt 작은 순으로 append되니가 heappop할 필요 없음...
                    #근데 for문을 순서대로 도는 게 최고의 방법이 아니라면...? 세번째자리수만 바꾸면 해결될 수도 있잖아.
                    #그래서 처음에 pop한 cnt에서 +1한 값으로 계속 넣는 거임.




#테스트 케이스 회수
t = int(input())
#9999까지 소수 판별 배열
prime = [True for _ in range(10000)]
#소수판별
findPrime()

for _ in range(t):
    start, end = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")