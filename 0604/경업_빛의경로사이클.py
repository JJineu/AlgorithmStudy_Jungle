from collections import deque

def solution(grid):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        grid[i] = list(grid[i])
    answer = []
    
    # flag, x, y, count 
    queue = deque()
    
    # x, y, flag 
    visited = [[[0 for _ in range(col)] for _ in range(row)] for _ in range(4)]
    #     상 하 좌 우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for i in range(row): # x
        for j in range(col): # y
            for k in range(4): # flag - 0: 상, 1: 하, 2: 좌, 3: 우
                if not visited[k][i][j]:
                    queue.append((k, i, j, 1)) # (flag, x, y, count)를 queue에 삽입
                    while queue:
                        flag, x, y, cnt = queue.popleft()

                        # 이미 방문 되었던 곳이라면 continue
                        if visited[flag][x][y]:
                            continue
                        
                        visited[flag][x][y] = 1 # 방문처리

                        # S, L, R 종류에 따른 다음 방문 좌표, flag 계산
                        if grid[x][y] == 'S':
                            nx = x + dx[flag]
                            ny = y + dy[flag]
                        # 상->우, 하->좌, 좌->상, 우->하
                        elif grid[x][y] == 'L':
                            if flag == 0:
                                nx = x
                                ny = y + 1
                                flag = 3
                            elif flag == 1:
                                nx = x
                                ny = y - 1
                                flag = 2
                            elif flag == 2:
                                nx = x - 1
                                ny = y
                                flag = 0
                            else:
                                nx = x + 1
                                ny = y
                                flag = 1
                        # 상->좌, 하->우, 좌->하, 우->상
                        else: # grid[x][y] == 'R'
                            if flag == 0:
                                nx = x
                                ny = y - 1
                                flag = 2
                            elif flag == 1:
                                nx = x
                                ny = y + 1
                                flag = 3
                            elif flag == 2:
                                nx = x + 1
                                ny = y
                                flag = 1
                            else:
                                nx = x - 1
                                ny = y
                                flag = 0
                        # nx, ny 보정 --> nx, ny가 음수일 때를 위해 더한 후 나머지 연산 진행
                        nx += row
                        nx %= row
                        ny += col
                        ny %= col

                        if visited[flag][nx][ny]:
                            answer.append(cnt)
                            continue
                        else:
                            queue.append((flag, nx, ny, cnt+1))
    # 정답 출력 조건에 따라 정렬   
    answer.sort()
    print(answer)
    # return answer

solution(["SL","LR"])
solution(["S"])
solution(["R","R"])
