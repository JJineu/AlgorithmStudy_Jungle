def solution(n, times):
    answer = 0

    left = 0
    right = max(times) * (n // len(times)) # //len(times)가 신기하네요

    while (left <= right):
        mid = (left + right) // 2
        cnt = 0
        
        for t in times:
            cnt += mid // t
        
        if cnt >= n:
            right = mid - 1
            answer = mid
            
        else:
            left = mid + 1

    return answer
