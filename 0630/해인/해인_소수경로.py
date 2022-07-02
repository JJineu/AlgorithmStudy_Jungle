import sys
input = sys.stdin.readline
from collections import deque
# 네 자리 중 한 자리의 숫자 바꿔보기
# 바뀐 수가 소수인지 확인
# 소수가 맞다면 q에 넣기
# pop 시킨 수가 목표한 수인지 확인 -> 맞으면 끝내기
# cnt 하나씩 올려주기

# 네자리 숫자인 소수들의 리스트 생성
sosu = []
for i in range(1000, 10000):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        sosu.append(i)

t = int(input())

num = [list(map(int, input().split())) for _ in range(t)]

def bfs(x, y):
    cnt = 0
    ans = 0 # 불가능한 경우 Impossible 출력
    q = deque()
    q.append((x, y))
    visited = [0 for i in range(10000)]
    visited[x] = 1
    
    while q:
        a, b = q.pop() # a: 현재 수, b: 목표 수
        # print(q)

        if a == b:
            return cnt
        
        cnt += 1
        
        # 네 자리 수 중 한 자리 수만 바꾸고 소수인지 확인
        strNow = str(a)
        num = 0
        # for i in range(10):
        #     num = int(tmp[0:3] + str(i))
        #     if num in sosu and num != a:
        #         q.append((num, y))
        # for i in range(10):
        #     num = int(tmp[0:2] + str(i) + tmp[3])
        #     if num in sosu and num != a:
        #         q.append((num, y))
        # for i in range(10):
        #     num = int(tmp[0] + str(i) + tmp[2:])
        #     if num in sosu and num != a:
        #         q.append((num, y))
        # for i in range(10):
        #     num = int(str(i) + tmp[1:])
        #     if num in sosu and num != a:
        #         q.append((num, y))
        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])

                if visited[tmp] == 0 and tmp in sosu and tmp >= 1000:
                    visited[tmp] = 1
                    q.append((tmp, b))


for i in range(t):
    print(bfs(num[i][0], num[i][1]))


# https://cijbest.tistory.com/13