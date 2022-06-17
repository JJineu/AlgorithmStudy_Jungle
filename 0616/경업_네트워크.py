from heapq import heappop, heappush

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)

    visit = [0 for _ in range(n+1)]
    queue = []

    def bfs():
        while queue:
            now = heappop(queue)
            visit[now] = 1

            for next in graph[now]:
                if not visit[next]:
                    heappush(queue, next)

    for i in range(1, n+1):
        if not visit[i]:
            heappush(queue, i)
            bfs()
            answer += 1

    # print(answer)
    return answer

def solution2(n, computers):
    # union - find
    tree = [1] * (n+1)
    parent = [0] * (n+1)
    for i in range(1, n+1): # 각 node의 부모 초기화
        parent[i] = i
    
    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x
    
    def union_parent(parent, a, b):
        if a < b:
            parent[b] = a
            tree[a] = tree[a] and tree[b]
        else:
            parent[a] = b
            tree[b] = tree[a] and tree[b]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                p1, p2 = find_parent(parent, i+1), find_parent(parent, j+1)

                if p1 == p2:
                    tree[p1] = 0
                else:
                    union_parent(parent, p1, p2)

    answer = 0
    for i in range(1, n+1):
        k = find_parent(parent, i)
        if k == i and tree[i]:
            answer += 1
    
    print(answer)
    return answer

def solution3(n, computers):
    answer = 0
    visit = [0 for _ in range(n+1)]
    queue = []

    def bfs():
        while queue:
            now = heappop(queue)
            visit[now] = 1

            for next in range(now+1, n+1):
                if computers[now-1][next-1] and not visit[next]:
                    heappush(queue, next)

    for i in range(1, n+1):
        if not visit[i]:
            heappush(queue, i)
            bfs()
            answer += 1

    print(answer)
    return answer

solution3(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
solution3(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1