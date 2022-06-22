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

# 220621 dfs를 이용한 첫 시도 (오답)

# 0은 벽이 있는 자리
# 1은 벽이 없는 자리 -> 이동 가능
# 게임 맵의 우측 하단 [n-1][m-1]에 도달해야
# 종료 조건
# 이미 방문한 곳의 경우 더이상 방문 X
# for문으로 상하좌우 이동
def solution(maps):
    n = len(maps)     # n: 행
    m = len(maps[0])  # m: 열
    def dfs(x, y):
        print('시작', x, y)
        print('시작', maps)
        if x == n-1 and y == m-1: 
            return
        # if maps[x][y] > 1:
        #     print('음')
        #     return
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            print(nx, ny, n-1, m-1)
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    dfs(nx, ny)
    dfs(0, 0)
    
    answer = maps[n-1][m-1]
    return answer

# bfs를 이용한 두번째 시도 (정답)
from collections import deque
def solution(maps):
    n = len(maps)    # n : 행
    m = len(maps[0]) # m : 열
    q = deque()
    q.append((0, 0))
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    answer = 0
    flag = False
    while q:
        x, y = q.popleft()
        
        # 종료 조건
        if x == n-1 and y == m-1:
            answer = maps[n-1][m-1]
            flag = True
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                q.append((nx, ny))
    if flag:      
        return answer
    else:
        return -1
