import sys
input = sys.stdin.readline
from collections import deque

R, C, K = map(int, input().split())
graph = [list(str(input().rstrip())) for _ in range(R)]
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1 #인덱스 매길 거니까
visited = [[1000] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((x1, y1))
visited[x1][y1] = 0 #시작점만 이걸로 업데이트해주기 (첫 조건문에서부터 비교해줄 거니까)

def bfs():
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nk = 1
            while 0<=nx<R and 0<=ny<C and graph[nx][ny] == '.' and nk <= K and visited[nx][ny] > visited[x][y]:
                if visited[nx][ny] == 1000: #이때만 visited[nx][ny] 업데이트할 거면 뭐하러 위에 조건문 달아줌...?
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1 #while문을 거듭해도 visited[x][y]는 아까 거.

                #같은 방향으로 가능하다면 전진
                nx += dx[i]
                ny += dy[i]
                nk += 1

bfs()
if visited[x2][y2]== 1004:
    print(-1)
else:
    print(visited[x2][y2])