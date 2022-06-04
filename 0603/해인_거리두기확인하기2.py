from collections import deque

def bfs(place): 
    start = []
    # place ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
    for i in range(len(place)):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j]) # 각 대기실별 탐색이 필요한 P 시작점들을 start에 넣어두고 시작
    # start [[0, 0], [0, 4], [2, 1], [2, 3], [4, 0], [4, 4]] [x좌표, y좌표]
    visited = [[False for _ in range(5)] for _ in range(5)]
    distance = [[0 for _ in range(5)] for _ in range(5)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # print(start[0][0], start[0][1])

    queue = deque() # 첫번째 P의 좌표를 넣어줌 
    queue.append((start[0][0], start[0][1]))
    visited[start[0][0]][start[0][1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[nx][ny] == False:
                # if place[nx][ny] == "P":
                #     return False
                # elif place[nx][ny] == "O" and
                if place[nx][ny] == "O":
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                elif place[nx][ny] == "P" and distance[x][y] <=  1:
                    return False
    
    return True

def solution(places):
    answer = []
    for place in places:
        if bfs(place): # bfs가 참이면 (거리두기가 잘 지켜지고 있으면)
            answer.append(1)
        else: # bfs가 거짓이면 (거리두기가 잘 지켜지고 있지 않으면)
            answer.append(0)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])