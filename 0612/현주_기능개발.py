from collections import deque

def solution(progresses, speeds):
    time = 0
    count = 0
    answer = []

    while progresses:
        if progresses[0] + speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count) #마지막까지 끝났을 때
    return answer
            
    # print(answer)


solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])