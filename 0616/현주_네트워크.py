import sys
sys.setrecursionlimit(1000000)

def solution(n, computers):
    count = 0
    visited = [0 for _ in range(n)]

    def dfs(i):
        visited[i] = 1
        for j in range(len(computers)):
            if j != i and computers[i][j] == 1 and not visited[j]:
                dfs(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    # print(count)
    return count
    


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])