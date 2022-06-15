import math
from heapq import heappop, heappush

'''이상한 dp로 풀다 경업이형 거 보고 이해함'''

def solution(n, works):
    answer = 0
    q = []
    for w in works:
        heappush(q, -w)

    while n:
        n -= 1
        if not q:
            break
        temp = heappop(q)
        if temp:
            temp += 1
            heappush(q, temp)
        else:
            heappush(q, 0)
    for i in q:
        answer += int(math.pow(i, 2))
    
    return answer

 
    
    # answer = 0
    # return answer




solution(4, [4, 3, 3])
