def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def solve(ans, cnt):
        nonlocal answer
        if n == cnt:
            if ans == target:
                answer += 1
            return
        
        solve(ans - numbers[cnt], cnt + 1)
        solve(ans + numbers[cnt], cnt + 1)

    solve(0, 0)
    # print(answer)
    return answer

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)
