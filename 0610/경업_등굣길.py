def solution(m, n, puddles):
    answer = 0

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    # dp[x][y]: flag - 오른쪽, 아래쪽
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

    solution(n, m)
    # for d in dp:
    #     print(d)
    print(dp[n][m])

solution(4, 3, [[2,2]])