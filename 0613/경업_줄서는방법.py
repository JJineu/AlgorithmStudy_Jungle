def factorial(dp, n):
    if n == 0:
        return 1

    dp[n] = n * factorial(dp, n-1)
    return dp[n]

def solution(n, k):
    people = [i for i in range(1, n+1)]
    answer = []
    dp = [1 for _ in range(n+1)]
    factorial(dp, n)
    # print(dp)
    
    while n > 0:
        fac = dp[n-1]
        tmp = [fac*i for i in range(1, n+1)]
        
        for i in range(1, n+1):
            if k <= tmp[i-1]:
                answer.append(people.pop(i-1))
                k -= fac * (i-1)
                break
        # print(f'    answer:{answer}, i: {i}, k: {k}, fac: {fac}')
        n -= 1
        print(answer)
    return answer

solution(3, 5) # 3, 1, 2
solution(4, 8) # 2, 1, 4, 3