# 화면 -> 클립보드 : 클립보드 비어있지 않아야 + 화면 개수로 대체
# 클립보드 -> 화면 : 화면 개수 + 클립보드 개수

# bfs : visited 처리 + q에 append
import sys
input = sys.stdin.readline
from collections import deque

s = int(input())
emoji = [[-1 for _ in range(s+1)] for _ in range(s+1)]
# emoji[a][b]: a는 화면에 출력된 이모지, b는 클립보드에 출력된 이모지
# s개의 이모지를 화면에 만드는데 걸리는 시간을 구해야 하므로 1부터 시작 -> s개일 때 완료

def bfs(n):
    q = deque()
    q.append((1, 0)) # 화면에 출력된 이모지, 클립보드에 출력된 이모지
    emoji[1][0] = 0 # 0초의 결과

    while q:
        a, b = q.popleft()
        
        if emoji[a][a] == -1:
            emoji[a][a] = emoji[a][b] + 1 # visited 처리
            q.append((a, a)) # q에 append
        if b > 0 and a+b <= n and emoji[a+b][b] == -1:
            emoji[a+b][b] = emoji[a][b] + 1
            q.append((a+b, b))
        if a - 1 > 0 and emoji[a-1][b] == -1:
            emoji[a-1][b] = emoji[a][b] + 1
            q.append((a-1, b))
    
    # print(emoji)
        
bfs(s)

ans = emoji[s][1]

for i in range(1, s+1):
    if ans > emoji[s][i]:
        ans = emoji[s][i]
        
print(ans)