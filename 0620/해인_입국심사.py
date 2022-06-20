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
