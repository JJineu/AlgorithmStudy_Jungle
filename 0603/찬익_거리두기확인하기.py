# 참고 자료 : https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python

    # 대기실 5개, 5*5
    # 파티션이 있다면 거리 2여도 가능
    # 지키면 1, 안지키면 0
    
    # 1. 2차원 배열 입력 받기
    # append 로 받아준 다음
    # a in b 로 한줄씩 bfs
    
    # 2. 탐색 방법
    # 입력 받은 값을 bfs로 탐색해서
    # P 주변으로 다른 P가 있는지 확인하고
    # 파티션 유무 확인 - 파티션 있으면 진행 안되도록
    
    # |r1 - r2| + |c1 - c2| - 2 <= 0  -> 이건 필요 없을듯
    # bfs로 상하좌우 탐색
    #   nx = x + dx[i]
    #   ny = y + dy[i]

    # 3. 조건 
    # 만족하면 1
    # 아니면 0 return
    
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5): 
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s]) 
        visited = [[0]*5 for i in range(5)]   
        distance = [[0]*5 for i in range(5)] 
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]  
            dy = [0, 0, -1, 1]  

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    elif p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer
