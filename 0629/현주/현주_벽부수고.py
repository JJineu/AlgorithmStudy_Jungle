import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, list(str(input().rstrip())))) for _ in range(R)]
visited = [[[0]*2 for _ in range(C)] for _ in range(R)]

q = deque()
q.append((0, 0, 1))
visited[0][0][1] = 1 #벽을 아직 안 부쉈을 때가  w = 1
#dp를 업데이트해주면 안되는 이유: 
#특정 노드까지 가는 최단경로가 최종목적지까지 벽을 1개만 부순 채 가지 못할수도.
#그러니까 그 노드까지 가는 최단경로라고 저장해놓고 그것보다 긴 경로는 못 들어오게 하는 풀이가 맞지 않는 문제인 것.
#하지만 부순 벽의 개수가 같을 때는 먼저 온 놈이 최단경로임........

def bfs():
    while q:
        x, y, w = q.popleft()
        
        if x == R-1 and y == C-1:
            return visited[x][y][w] #근데 w가 0일때, 1일때 둘 다 비교해줘야 하는 거 아님?
                                    #bfs라 아닐듯
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny] == 1 and w == 1: #벽을 만났는데 아직 0으로 안 건너갔다
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))
            
    return -1

answer = bfs()
print(answer)




'''visited 대신 dist만 쓴 풀이, 자꾸 21%에서 틀림'''
# dp = [[-1]*C for _ in range(R)]
# q = deque()
# q.append([0, 0, 0])
# dp[0][0] = 1

# def bfs():
#     answer = -1
#     while q:
#         x, y, broken_walls = q.popleft()
#         # print(f'popped {x, y, broken_walls}')
#         if x == R-1 and y == C-1:
            # print(dp[x][y])

#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<R and 0<=ny<C:
#                 if dp[nx][ny] == -1 or dp[nx][ny] > dp[x][y] + 1:
#             # if 0<=nx<R and 0<=ny<C and dp[nx][ny] == -1:
#                     if graph[nx][ny] == 0:
#                         dp[nx][ny] = dp[x][y] + 1
#                         q.append([nx, ny, broken_walls])
#                     else: #graph[nx][ny] == 1 (벽)
#                         if broken_walls < 1:
#                             dp[nx][ny] = dp[x][y] + 1
#                             q.append([nx, ny, broken_walls + 1])
                        
#                             # print(-1)
#                             # Flag = False
#                             # break

#     print(answer)

# bfs()