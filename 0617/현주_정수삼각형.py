def solution(triangle):
    t = len(triangle)
    dp = [[0 for _ in range(len(row))]for row in triangle]
    # print(dp)
    
    def dfs(row, i):
        # print(f'row: {row}, i: {i}')
        if dp[row][i]:
            return dp[row][i]
            
        if row == 0:
            dp[row][i] += triangle[0][0]
            # print(dp)
            return dp[row][i]

        if i == 0: #i == 0
            dp[row][i] += dfs(row-1, i) + triangle[row][i]
        elif i == len(triangle[row])-1:
            dp[row][i] += dfs(row-1,i-1) + triangle[row][i]
        else:
            dp[row][i] += max(dfs(row-1, i-1) + triangle[row][i], dfs(row-1, i) + triangle[row][i])
        
        # print(dp[row][i])
        return dp[row][i]
        
    biggest = 0
    for i in range(len(triangle[-1])):
        result = dfs(t-1, i)
        # print(result)
        if result > biggest:
            biggest = result
            
    # print(biggest)
    return biggest
        # dp[row][i] = 
        # dp[row-1][i-1] + triangle[row][i]
        # dp[row-1][i] + triangle[row][i]


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])