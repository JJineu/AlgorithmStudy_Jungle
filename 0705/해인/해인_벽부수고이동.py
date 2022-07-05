import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

road = [[] for _ in range(n)]

for i in range(n):
    road[i] = list(map(int, input().strip()))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# visited[x][y][0] : 벽 파괴 기회를 사용하지 않은 경우 신호 -> 0
# visited[x][y][1] : 벽 파괴 기회를 사용한 경우 신호 -> 1
# visited[x][y][z] 가 나타내는 값 -> (x, y)까지 이동 횟수
# 벽 파괴 기회를 사용한 경우 : [x][y][1]에 이동 횟수 저장됨
# 벽 파괴 기회를 사용하지 않은 경우 : [x][y][0]에 저장됨

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    visited[x][y][z] = 1 # 이동횟수 갱신
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, c = q.popleft()

        if a == n-1 and b == m-1: # 종료 조건 반드시 필요
            return visited[a][b][c]

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                # 벽이고 벽을 파괴한 적이 없을 경우 -> 방문 가능
                if road[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                # 벽이 아닐 때 방문한 적 없을 경우 -> 방문 가능
                elif road[nx][ny] == 0 and visited[nx][ny][c] == 0: # 넘어온 게 벽인지 아닌지 모름
                    visited[nx][ny][c] = visited[a][b][c] + 1 # 벽을 부쉈는지 안 부쉈는지 모름
                    q.append((nx, ny, c)) # 벽을 부쉈는지 안 부쉈는지 모름
    return -1

print(bfs(0, 0, 0)) # 벽 파괴 횟수를 사용하지 않음
