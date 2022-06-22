def solution(n, times):
    answer = 0
    
    times.sort()
    start = 0
    end = max(times) * n

    while start <= end :
        mid = (start + end) // 2
        tmp = 0
        for t in times:
            tmp += mid // t  
            # 총 시간 // 몇분 -> 몇 사람을 처리할 수 있는지
        if tmp >= n: # tmp가 더 작아져야 하므로 end = mid - 1
            end = mid - 1
            answer = mid
        if tmp < n: # tmp가 더 커져야 하므로 start = mid + 1
            start = mid + 1

    return answer

# 220621 다시 풀어보기

# n : 입국심사를 기다리는 사람 수
# times : 각 심사관이 한 명을 심사하는데 걸리는 시간
# max times : n * min(times)
# max times // times : 입국심사 완료한 사람 수 -> 총합이 n보다 작으면 max times가 더 커져야
# 총합이 n보다 크면 max times가 작아져야
def solution(n, times):
    start = 1
    end = n * min(times)
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
        
        if cnt < n: # cnt가 더 커져야 -> mid가 더 커져야
            start = mid + 1
        else: # cnt >= n cnt가 더 작아져야 -> mid가 더 작아져야
            end = mid - 1
            answer = mid
    
    return answer
