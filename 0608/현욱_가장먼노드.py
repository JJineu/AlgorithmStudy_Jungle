from collections import deque

def solution(n, edge):

    graph = [ [] for i in range(n+1) ]
    visited = [0] * (n+1)

    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)

    visited[1] = 1
    q = deque([1])

    while q :
        x = q.popleft()
        for i in graph[x] :
            if not visited[i] :
                visited[i] = visited[x] + 1
                q.append(i)

    maxvalue = max(visited)

    count = visited.count(maxvalue)

    return count if count > 0 else 0