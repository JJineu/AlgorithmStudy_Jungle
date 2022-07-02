import sys
input = sys.stdin.readline
from collections import deque

col, row = map(int, input().split())
graph = [list(str(input().rstrip())) for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * (col+1) for _ in range(row+1)]

def bfs(x, y):
    global col, row
    blue = 0
    white = 0
    q = deque()
    q.append([x, y])
    
    while q:
        r, c = q.popleft()
        if not visited[r][c]: #이거 확인 안해서 틀리는 중이었음;;; 장난하냐 (중복해서 append될 수 있음)
            visited[r][c] = 1

            if graph[r][c] == 'W':
                white += 1
            else:
                blue += 1

            for i in range(4):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    if graph[r][c] == graph[nx][ny]:
                        q.append([nx, ny])
                        # print(f'blue = {blue}, white = {white}')
    return blue, white

blue_strength = 0
white_strength = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            # print(f'새로 드간다 at ({i, j})')
            blue, white = bfs(i, j)
            blue_strength += blue**2
            white_strength += white**2
print(white_strength, blue_strength, sep = ' ')