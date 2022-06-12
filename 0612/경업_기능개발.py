def solution(progresses, speeds):
    answer = []

    day = 1
    while progresses:
        cnt = 0
        while progresses[0] + day*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)            
            cnt += 1

            if not progresses:
                break
        
        if cnt:
            answer.append(cnt)
        day += 1
    return answer

solution([93, 30, 55],	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])