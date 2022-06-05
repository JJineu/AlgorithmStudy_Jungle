import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

#상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(5)] for _ in range(5)]
# print(visited)

def check(room, x, y, depth=0):
    visited[x][y] = 1
    if depth == 2:
        return True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if visited[nx][ny]: continue
            if room[nx][ny] == 'P':
                return False
            elif room[nx][ny] == 'O':
                check(room, nx, ny, depth+1)
            # else: continue #벽이면 다른 방향 탐색
    return True

def solution(slist):
    answer = []
    for room in slist: #["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] 즉 각 교실
        Flag = False
        for x in range(5):
            for y in range(5):
                if room[x][y] == 'P':
                    if not check(room, x, y, 0):
                        print(check(room, x, y, 0))
                        answer.append(0)
                        Flag = True
                        break
            if Flag:
                break
        else: 
            answer.append(1)
        print(answer)

    # print(answer)
    return answer
    



solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# solution([["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"], ["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# solution(["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"])
# ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]