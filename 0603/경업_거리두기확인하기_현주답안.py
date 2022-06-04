#상, 하, 좌, 우
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def solution(slist):
    answer = []
    for room in slist: #["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] 즉 각 교실

        Flag = True
        visited = [[0 for _ in range(5)] for _ in range(5)]
        def check(x, y, depth=0):
            visited[x][y] = 1

            nonlocal Flag
            if depth == 2:
                return

            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if 0 <= dx < 5 and 0 <= dy < 5:
                    if visited[dx][dy]:
                        continue

                    if room[dx][dy] == 'P':
                        Flag = False
                        return
                    elif room[dx][dy] == 'O':
                        check(dx, dy, depth + 1)
        
        for x in range(5):
            for y in range(5):
                if room[x][y] == 'P':
                    check(x, y, 0)
                if not Flag:
                    break
            if not Flag:
                break         

        if Flag:
            answer.append(1)
        else:
            answer.append(0)

    print(answer)
    return answer
    



solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
solution([["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"], ["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# solution(["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"])
# ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]