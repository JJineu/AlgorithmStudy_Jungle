from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # visit = list([0]*m for _ in range(n))
    q = deque([[0,0]])
    # q = [[0,0]]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x, y = q.popleft()
        # x,y = q.pop(0)
        if x == n-1 and y == m-1:
            return maps[-1][-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx,ny])
    return -1