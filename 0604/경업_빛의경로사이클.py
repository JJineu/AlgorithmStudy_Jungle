from collections import deque

def solution(grid):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        grid[i] = list(grid[i])
    answer = []

    # S에 도달할 경우 직진
    # L에 도달할 경우 좌회전
    # R에 도달할 경우 우회전
    # 빛이 격자의 끝을 넘어가면 반대쪽으로 돌아옴
    
    queue = deque()
    queue.append((0, 0, 0, 1)) # in/out, x, y, count
    visited = [[[0 for _ in range(col)] for _ in range(row)] for _ in range(4)]
    #     상 하 좌 우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while queue:
        # flag 0~3: in - 상하좌우
        flag, x, y, cnt = queue.popleft()
        print(f'flag: {flag}, x: {x}, y: {y}, cnt: {cnt}')
        if visited[flag][x][y]:
            continue

        visited[flag][x][y] = 1

        if grid[x][y] == 'S':
            nx = x + dx[flag] + row
            nx %= row
            ny = y + dy[flag % 4] + col
            ny %= col
            # 순환 끝
            if visited[flag][nx][ny]:
                print(cnt)
                continue
            else:
                queue.append((flag, nx, ny, cnt+1))
        elif grid[x][y] == 'L':
            # 상->우, 하->좌, 좌->상, 우->하
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
            nx += row
            nx %= row
            ny += col
            ny %= col
            
            # 순환 끝
            if visited[flag][nx][ny]:
                print(cnt)
                continue
            else:
                queue.append((flag, nx, ny, cnt+1))
        else:
            # 상->좌, 하->우, 좌->하, 우->상
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
            nx += row
            nx %= row
            ny += col
            ny %= col

            # 순환 끝
            if visited[flag][nx][ny]:
                print(cnt)
                continue
            else:
                queue.append((flag, nx, ny, cnt+1))

    print(visited)
    return answer

solution(["SL","LR"])
solution(["S"])
solution(["R","R"])
