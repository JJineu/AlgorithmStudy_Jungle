# 정답 참고
# https://dev-note-97.tistory.com/141

# m n 리스트를 만든다
# m n list에서 puddles 처리
# 최단 거리 구해야됨
# 오른쪽, 아래로만 움직임
# 이동 경우의 수 = 위, 왼쪽 블록까지의 이동 경우의 합
# 이동 경우의 수를 dp로 저장

def solution(m, n, puddles):    
    puddles = [[q,p] for [p,q] in puddles] # 행렬 반대로 주어지므로, 반대로 뒤집어줌
    dp = [[0] * (m + 1) for i in range(n + 1)]  # 열 : m, 행 : n
    dp[1][1] = 1 # 시작점 1로 최기화
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: # 시작점
                continue 
            if [i, j] in puddles:  # puddle이면 dp = 0 -> 이동 불가
                dp[i][j] = 0
            else: # 이동 가능하면 전까지의 이동 경우를 합해서 dp에 넣어둠
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
                
    return dp[n][m] # 도착점 (끝점)까지의 경우의 수를 return