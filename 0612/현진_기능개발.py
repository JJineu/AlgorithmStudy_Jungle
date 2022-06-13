# 같은날 배포되는 기능의 개수

def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    
    day = 0
    cnt = 0
    while progresses:
        
        # for i in range(n):
        if progresses[0] + speeds[0] * day < 100:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
        else:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
    answer.append(cnt)
    # print(answer)
    return answer

solution([93, 30, 55],	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])