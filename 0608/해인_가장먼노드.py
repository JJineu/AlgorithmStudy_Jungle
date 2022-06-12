# 노드의 개수 n
# 간선에 대한 정보가 담긴 배열 vertex
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지 return
# 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들
from collections import deque

def bfs(s, graph, visited, dist):
    q = deque()
    q.append([s, 0])
    visited[s] = True

    while q:
        v, d = q.popleft()
        dist[v] = d
        
        for i in graph[v]:
            if not visited[i]:
                q.append([i, d+1])
                visited[i] = True

    return dist.count(max(dist))

def solution(n, vertex):
    graph = [[0]] + [[] for _ in range(n)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n+1)
    dist = [0 for _ in range(n+1)]
    mid = bfs(1, graph, visited, dist)
    return mid
    