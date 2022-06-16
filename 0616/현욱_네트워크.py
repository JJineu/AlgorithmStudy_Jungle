def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * (n)
    count = 0

    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(i)
            else :
                continue

    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for j in range(len(visited)) :
        if visited[j] == False :
            dfs(j)
            count = count + 1
    print(count)
    return count

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])