import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
visited = [[0] * C for _ in range(R)]
# print(visited)

dx = [-1, 0, 1, 0] #북, 우, 남, 서
dy = [0, 1, 0, -1]

for _ in range(R):
    graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1 #현재 위치를 청소한다

while 1:
    flag = 0
    for _ in range(4):
        #d=0일 때 3-2-1-0 순서로 탐색
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4

        if 0<= nx < R and 0<=ny < C and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            r = nx
            c = ny
            cnt += 1
            flag = 1
            break #청소했으니 이제 새로 시작 inside while loop

    if flag == 0:
        if graph[r-dx[d]][c-dy[d]] == 1: #후진 못함
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d] #후진하고 다시 while문

