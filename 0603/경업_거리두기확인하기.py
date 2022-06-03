from collections import deque

def solution(places):
    answer = []

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    for place in places:
        # 사람의 위치를 리스트에 담고
        people = deque()
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people.append((i, j))
        
        # flag 1: 거리두기 지킴, 0: 안지킴
        flag = 1 

        # 각 사람이 되는지 안되는지를 체크해보자
        while people:
            if flag == 0: # 규칙 안지킨 회의실임이 확인되었으면 break
                break

            x, y = people.popleft()

            for i in range(4):
                if flag == 0: # 규칙 안지킨 회의실임이 확인되었으면 break
                    break

                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5:
                    if place[nx][ny] == 'P':
                        flag = 0 # 규칙 안지킨 회의실이다
                        break
                    elif place[nx][ny] == 'X': # 파티션이 있는 방향은 문제 없음
                        continue
                    else: # 파티션이 없는 경우 사람을 체크해야 한다
                        for i in range(4):
                            nnx = nx + dx[i]
                            nny = ny + dy[i]

                            # 원래 사람이 있던 곳은 패스
                            if nnx == x and nny == y:
                                continue

                            if 0 <= nnx < 5 and 0 <= nny < 5:
                                if place[nnx][nny] == 'P':
                                    flag = 0 # 규칙 안지킨 회의실이다
                                    break
        answer.append(flag)
    
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])