# (1,1) -> (m,n)
# 최단경로의 개수 % 1000000007
# 오른쪽(x+1, y) x+1 <= m , 아래(x,y+1) y+1 <= n 로만 갈 수 있음
# x+1 = m 혹은 y+1 =n 만나면 경로가 하나로 정해짐
# 물 있는지 확인.

# 시간초과 -> 통과

def solution(m, n, puddles):

    # graph = [[0]*(m+1) for _ in range(n+1)]

    d = [[0]*(m+1) for _ in range(n+1)]
    # d[1][2] = 1 # 물웅덩이가 있을 수 있음
    # d[2][1] = 1
    d[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1: continue
            for x,y in puddles:
                d[y][x] = 0
            d[i][j] = d[i-1][j] + d[i][j-1]        

    # print(d[n][m])       
    return d[n][m] % 1000000007