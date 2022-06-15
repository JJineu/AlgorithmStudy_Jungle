# 야근 피로드 = (남은 일의 작업량) 제곱의 합
# N시간 동안 야근 피로도 최소화
# 1시간 -> 작업량 1
# N : 퇴근까지 남은 시간, works : 각 일에 대한 작업량 
# 야근 피로도 최소화하는 시간 리턴
from heapq import heappop, heappush
def solution(n, works):
    hp = []
    for i in works:
        heappush(hp, [-i, i])
    # heap [[-2, 2], (-1, 1), (-2, 2)]
    cnt = 0
    while cnt < n:
        num = heappop(hp)[1]
        if num >= 1:
            heappush(hp, [-num+1, num-1])
        else:
            heappush(hp,[0,0])
        cnt += 1
    answer = 0
    while hp:
        answer += heappop(hp)[1]**2
    
    return answer
