# 오른쪽과 아래쪽으로만 움직임
# 집에서 학교까지 갈 수 있는 최단경로 개수 % 1000000007
from collections import deque
def bfs(x, y, road, visited, m, n):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    dx = [1, 0]
    dy = [0, 1]
    answer = 0
    while dq:
        cx, cy = dq.popleft()
        exist = road[cx][cy] # 기존 길의 값
        for i in range(2):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m-1 and 0 <= ny <= n-1:
                if not visited[nx][ny] and road[nx][ny] != -1:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    road[nx][ny] = exist + 1
                    print(road)
    
    return road[n-1][m-1]
                    
                

def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]
    for a, b in puddles:
        road[a-1][b-1] = -1 # 물 웅덩이가 있는 좌표의 값은 -1로 만들어줌
    # road [[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0]]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    return bfs(0, 0, road, visited, m, n)
    
