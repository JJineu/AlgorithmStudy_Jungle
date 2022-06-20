def solution(n, times):
    answer = 0

    pl = 0
    pr = max(times) * (n // len(times))

    while (pl <= pr):
        pc = (pl + pr) // 2

        cnt = 0
        for time in times:
            cnt += pc // time
        
        print(cnt)
        if cnt >= n:
            pr = pc - 1
            answer = pc
        else:
            pl = pc + 1

    return answer

solution(6, [7, 10])