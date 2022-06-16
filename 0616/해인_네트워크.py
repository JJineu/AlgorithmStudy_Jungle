# 컴퓨터의 개수 n
# 연결에 대한 정보 computers -> i와 j가 연결되어 있으면 1
# return : 네트워크 개수
# computers[i][i]는 항상 1
def dfs(v, computers, visited, n):
    for i in range(n):
        if computers[v][i]: # 연결되어 있다면
            if not visited[i]: # 방문할 수 있다면
                visited[i] = True
                dfs(i, computers, visited, n)
            
def solution(n, computers):
    visited = [0 for _ in range(n)] # 점 하나만 방문한 여부를 알면 되므로 1차원 visited 써야 함!
    
    cnt = 0
    for v in range(n): # 0, 1, 2 방문
        if not visited[v]: # 연결, 방문할 수 있을 때
            visited[v] = 1
            dfs(v, computers, visited, n) # 0 들어왔을 때 0, 1, 2 다 방문해서 1과 2는 사이클 돌지 않음
            cnt += 1

    return cnt
