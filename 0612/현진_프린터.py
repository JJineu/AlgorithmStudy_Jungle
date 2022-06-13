from collections import deque

def solution(priorities, location):
    answer = []
    q = deque([])
    for i in enumerate(priorities):
        q.append(i)
    # deque([(0, 2), (1, 1), (2, 3), (3, 2)])


    while q:
        index = 0
        
        # 우선순위가 가장 큰 인덱스를 찾음
        for i in range(len(q)):
            if q[i][1] > q[index][1]:
                index = i
                
        q.rotate(-index)     
        answer.append(q.popleft())

        if answer[-1][0] == location:
            break

    return len(answer)