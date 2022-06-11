def solution(m, n, puddles): # m은 열, n은 행
    cur = [[-1 for _ in range(m)] for _ in range(n)] # n행 m열, 방문하지 않았을 때 -1 
    cur[0][0] = 1
    
    def dfs(x, y):
        print(f'x:{x}, y:{y}')
        if x < 0 or y < 0:
            return 0
        if cur[x][y] != -1: # 방문한 적 있으면 그 곳에서 목적지까지 도달했던 경로 수 리턴받고 재귀 안 돎  
            return cur[x][y]
        if [x, y] in puddles:
            return 0
        
        up = dfs(x-1, y)
        left = dfs(x, y-1)
        
        cur[x][y] = (up + left) % 1000000007
        return cur[x][y]
    
    dfs(2, 3)
    
    for c in cur:
        print(c)
    
    return cur[n-1][m-1]

solution(4, 3, [[2,2]])
