def solution(m, n, puddles):
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    
    dp[1][1] = 1
    def solution(x, y):
        if x < 1 or y < 1:
            return 0
        if dp[x][y] != -1:
            return dp[x][y]
        if [x, y] in puddles:
            return 0
        
        up = solution(x-1, y)
        left = solution(x, y-1)

        dp[x][y] = (up + left) % 1000000007
        return dp[x][y]

    solution(m, n)
    for d in dp:
        print(d)
    # print(dp[m][n])
    return dp[m][n]

solution(4, 3, [[2,2]])