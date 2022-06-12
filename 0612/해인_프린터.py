def solution(priorities, location):
    p = list(enumerate(priorities))
    cur = p[location]
    order = 0
    answer = []
    while p:
        cri = p.pop(0) # 맨 첫번째 값
        for i in range(0, len(p)):
            if cri[1] < p[i][1]: # 남아있는 우선순위 값이 더 큰 게 있을 때
                p.append(cri)
                break
        else:
            order += 1
            if cri == cur:
                return order
            
            
    #         answer.append(cri)
    # for i in range(len(answer)):
    #     if answer[i][0] == location-1:
    #         return i+1
