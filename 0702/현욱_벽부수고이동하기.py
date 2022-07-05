from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for _ in range(N):
    data.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 다음 이동할 곳이 벽이고, 벽을 한번도 부시지 않은 경우
            if data[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 한 번도 방문하지 않은 곳
            elif data[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


print(bfs(0, 0, 0))
