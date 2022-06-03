# 못품
from collections import deque

q = deque()
def solution(places):
    for i in range(5):
        for j in range(5):
            k = places[i][j]
            print(k)
        bfs(places[i])
    # answer = []
    return 

def bfs(x,y):
    res = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]        
    visit = [[0]*5 for i in range(5)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and visit[nx][ny] == 0:
                q.append([nx][ny])
                visit[nx][ny] = 1
    return res

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)
