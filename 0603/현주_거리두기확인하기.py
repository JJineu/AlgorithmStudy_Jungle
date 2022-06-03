import sys
input = sys.stdin.readline

#상, 하, 좌, 우
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

def solution(slist):
    answer = []
    for room in slist: #["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] 즉 각 교실
        seats = []
        for row in room:
            seats.append(list(row)) #"POOOP" -> ['P', 'O', 'O', 'O', 'P']
        
        def check(x, y, depth=0):
            if depth ==  2:
                return True

            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if 0 <= dx < 5 and 0 <= dy < 5:
                    if room[dx][dy] == 'P':
                        return False
                    elif room[dx][dy] == 'O':
                        depth += 1
                        check(dx, dy, depth)
                    else: return True #벽이면
            # return True
        
        Flag = False
        for x in range(5):
            for y in range(5):
                if room[x][y] == 'P':
                    if check(x, y, 0):
                        continue
                    else:
                        answer.append(0)
                        Flag = True
                        break
            if Flag:
                break
        else: 
            answer.append(1)

    print(answer)
    return answer
    



solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
solution([["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"], ["PPPPP", "PPPPP", "PPPPP", "PPPPP", "PPPPP"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# solution(["OPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"])
# ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]