def solution(t):
    for i in range(len(t)):
        t[i] = [0] + t[i] + [0]
        # t〉[[0, 7, 0], [0, 3, 8, 0], [0, 8, 1, 0, 0], [0, 2, 7, 4, 4, 0], [0, 4, 5, 2, 6, 5, 0]]
    dp = [[] for _ in range(len(t))]
    for i in range(len(t)):
        dp[i] = [0 for _ in range(i+3)]
        # dp [[0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    
    if len(t) == 1:
        return t[0][1]
    else :
        dp[0][1] = t[0][1]
        
        for i in range(1, len(t)):
            for j in range(1, i+2): # 처음과 끝에 0을 둔 곳은 따로 dp 값 갱신하지 않고 처음 0인 곳과 마지막 0인 곳은 제외하고 dp값 계산해줌
                dp[i][j] = max(dp[i-1][j-1] + t[i][j], dp[i-1][j] + t[i][j])
        
        return max(dp[-1])
