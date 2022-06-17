# 경업이형은 왜 dp를 좋아하는걸까...

# 트리 상단부터 하나씩 내려오면서 좌, 우 중 경로로 진행
# 트리 끝까지 진행하면 멈춤

# 경우의 수 
# 2 ** n-1층

# 각 경우의 수를 저장하면서 내려가야 함
# 점화식을 만들어보자

def solution(triangle):
    depth = len(triangle)
    dp = [] 
    
    for _ in range(depth-1): # depth 만큼 dp를 만들어줌
        dp.append([])
            
    dp.append(triangle[depth-1]) # 맨 아래층을 dp에 넣어줌, 아래에서 부터 bottom-up으로 합 dp 만들기 위함

    for i in range(depth - 2, -1, -1): # 맨아래층 넣었으니까, 그 다음층부터, 역순으로
        rowCnt = i + 1 # 해당 층의 크기 (인자가 몇개인가)

        for j in range(0, rowCnt): # 해당 층 인자수만큼 for문 돌리면서 더해봄
            dp[i].append(max(dp[i+1][j] + triangle[i][j], dp[i+1][j+1] + triangle[i][j]))

    answer = dp[0][0] # 최상단 = 결과값
    return answer
