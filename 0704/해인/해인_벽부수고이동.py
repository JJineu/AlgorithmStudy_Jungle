# 0은 이동 가능
# 1은 이동 불가 벽
# 1, 1 ~ N, M -> 최단경로로 이동
# 시작 칸, 끝나는 칸 모두 포함
# 벽을 부수고 이동하는 게 더 빠르면 벽을 한 개까지 부수고 이동
# 불가능 시 -1 출력
# 상하좌우 인접
# 최단 경로?
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

road = [[] for _ in range(n+1)]

for i in range(1, n+1):
   road[i] = [-2] + list(map(int, input().strip()))

def bfs(x, y, br):
    q = deque()
    q.append((x, y, br))
    # cnt = 0
    visited = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    visited[x][y] = 1
    
    while q:
        a, b, brcnt = q.popleft()
        if x == n and y == m:
            return
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m:
                if visited[nx][ny] == -1 and road[nx][ny] == 0:
                    visited[nx][ny] = 1
                    road[nx][ny] = road[a][b] + 1
                    # print('들어옴1', nx, ny, visited[nx][ny], road[nx][ny])
                    q.append((nx, ny, br))
                elif visited[nx][ny] == -1 and road[nx][ny] == 1:
                    if brcnt == 0:
                        visited[nx][ny] = 1
                        road[nx][ny] = road[a][b] + 1
                        # print('들어옴2', nx, ny, visited[nx][ny], road[nx][ny])
                        q.append((nx, ny, br+1))


bfs(1, 1, 0)
print(road)
print(road[6][4])


# print("em", nx, ny, road[nx][ny])
#                 if road[nx][ny] == 0:
#                     road[nx][ny] = road[a][b] + 1
#                     print('들어옴1', nx, ny, road[nx][ny])
#                     q.append((nx, ny, br))
#                 elif road[nx][ny] == 1:
#                     if brcnt == 0:
#                         road[nx][ny] = road[a][b] + 1
#                         print('들어옴2', nx, ny, road[nx][ny])
#                         q.append((nx, ny, 1))