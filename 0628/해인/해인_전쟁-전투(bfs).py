# bfs 풀이는 시간이 108ms 나옴
# dfs 풀이는 시간이 88ms 나옴

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # m : 행, n : 열

war = [list(input().rstrip()) for _ in range(m)]

# [['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], 
#  ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']]

visited = [[0 for _ in range(n)] for _ in range(m)]
wcnt, bcnt = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1 # visited 처리 (1)
    cnt = 1 # 자기 자신도 방문한 것이므로 cnt는 1부터 시작

    while q:
        a, b = q.pop()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx <= m-1 and 0 <= ny <= n-1: # 범위 안에 있을 경우
                if war[nx][ny] == color and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1 # visited 처리 (2)
                    cnt += 1

    return cnt


for i in range(m):
    for j in range(n):
        if war[i][j] == 'W' and not visited[i][j]:
            wcnt += bfs(i, j, 'W') ** 2
        elif war[i][j] == 'B' and not visited[i][j]:
            bcnt += bfs(i, j, 'B') ** 2

print(wcnt, bcnt)
