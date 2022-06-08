from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    m = len(graph)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    for g in graph:
        print(g)

    # 1번 노드 방문처리
    visit[1] = 1
    queue = deque()
    queue.append((1, 0)) # (node, distance)

    while queue:
        now, d = queue.popleft()
        dist[now] = d

        for next in graph[now]:
            if not visit[next]:
                visit[next] = 1
                queue.append((next, d+1))
                
    print(dist)
    print(dist.count(max(dist)))
    
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [1, 4]])