def solution(triangle):
    n = len(triangle)
    dp = []
    for t in triangle:
        dp.append([0 for _ in range(len(t))])
    
    def recur(i, j):
        if i < 0:
            return 0
        if j < 0 or j > i:
            return 0        
        if dp[i][j]:
            return dp[i][j]

        right = recur(i-1, j)
        left = recur(i-1, j-1)
        dp[i][j] = max(left, right) + triangle[i][j]
        return dp[i][j]

    dp[0][0] = triangle[0][0]
    for k in range(n):
        recur(n-1, k)
    
    # for d in dp:
    #     print(d)

    return max(dp[-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) # 30