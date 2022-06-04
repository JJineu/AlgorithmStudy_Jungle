from collections import deque

def bfs(place): 
    start = []
    # place ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i, j]) # 각 대기실별 탐색이 필요한 P 시작점들을 start에 넣어두고 시작
    # start [[0, 0], [0, 4], [2, 1], [2, 3], [4, 0], [4, 4]] [x좌표, y좌표]


    for s in start:
        queue = deque([s]) # 첫번째 P의 좌표를 넣어줌 
        # 시작점별로 방문처리와 거리계산을 새로 해줘야 하므로 
        # for문 안에 visited와 distance를 둠
        visited = [[False for _ in range(5)] for _ in range(5)]
        distance = [[0 for _ in range(5)] for _ in range(5)]
        queue.append((s[0], s[1]))
        visited[s[0]][s[1]] = True

        while queue:
            y,  x = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx <= 4 and 0 <= ny <= 4 and visited[ny][nx] == False:
                    if place[ny][nx] == "O":
                        queue.append([ny, nx])
                        visited[ny][nx] = True
                        distance[ny][nx] = distance[y][x] + 1
                    elif place[ny][nx] == "P" and distance[y][x] <=  1:
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

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))