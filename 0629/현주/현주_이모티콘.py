import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
# 2<= S <= 1000

q = deque()
q.append((1,0))
dist = [[-1]*(N+1) for _ in range(N+1)]
dist[1][0] = 0
#꼭 카운트가 커지는 순으로 들어가는 게 아니라 그저 dp일 뿐...
#최초의 한 번만 업데이트하기 때문에 그 dist[s][c]의 최소값일 수밖에 없음
#또한, 세 개의 모션은 독립적임. 꼭 세 개가 번갈아가며 연속적으로 수행될 필요 X.
while q:
    s, c = q.popleft()
    #화면 -> 클립보드에 복사
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    #클립보드 -> 기존 화면 + 클립보드
    if s + c <= N and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    #화면에서 하나 삭제
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
    
answer = -1
for i in range(N+1):
    if dist[N][i] != -1:
        if answer == -1 or answer > dist[N][i]:
            answer = dist[N][i]

print(answer)