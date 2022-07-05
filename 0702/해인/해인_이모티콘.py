# 이미 화면에 이모티콘 1개 입력된 상태
# 3가지 연산만 -> 이모티콘 S개
# S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
emoji = [[-1 for _ in range(n+1)] for _ in range(n+1)] 
# emoji[a][b] : a는 화면에 출력된 이모지, b는 클립보드에 출력된 이모지
# 화면에 출력된 이모지는 1부터 시작하므로 n+1로 함

def bfs(n):
    q = deque()
    q.append((1, 0)) # 화면:1, 클립보드:0
    emoji[1][0] = 0
    
    while q:
        a, b = q.popleft()
        if emoji[a][a] == -1:
            q.append((a, a))
            emoji[a][a] = emoji[a][b] + 1
            # print(a, b, emoji[a][b], emoji[a][a])      # 그곳까지 도달하는데 걸린 시간 + 1
        if a+b <= n and emoji[a+b][b] == -1:
            q.append((a+b, b))
            emoji[a+b][b] = emoji[a][b] + 1
            # print(emoji[a][b],emoji[a+b][b]) 
        if a > 0 and emoji[a-1][b] == -1:
            q.append((a-1, b))
            emoji[a-1][b] = emoji[a][b] + 1
            # print(emoji[a][b],emoji[a-1][b]) 
        


bfs(n)
ans = -1
for i in range(1, n+1):
    if ans == -1 or ans > emoji[n][i]:
        ans = emoji[n][i]

print(ans)