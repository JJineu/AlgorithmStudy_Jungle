# 피로도 = sum(야근 시작 시점에서 남은 일의 작업량 ** 2)
# 퇴근까지 남은 N 시간
# 각 일에 대한 작업량 works

def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    
    while n:
        if works[0] == 0:
            break
        
        for i in range(len(works)):
            if n == 0 or works[0] > works[i]:
                 break
             
            works[i]-=1
            n -= 1

    for i in works:
        answer+=i*i 

    return answer