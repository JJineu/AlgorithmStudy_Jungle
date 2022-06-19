import heapq
from heapq import heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    # print(maps)
    row = len(maps)
    col = len(maps[0])
    # print(row, col)
    
    q = [[maps[0][0], 0, 0]]
    while q:
        mov, x, y = heappop(q)
        #print((mov, x, y))
        #종료조건
        if x == row-1 and y == col-1:
            # print(mov)
            return mov
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1:
                maps[nx][ny] += mov
                heappush(q, [maps[nx][ny], nx, ny])
                #heappush(q, [mov+1, nx, ny])
                #print(q)

    # print(-1)
    return -1



# solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])