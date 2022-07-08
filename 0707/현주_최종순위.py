import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    last_year = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    inDegree = [0]*(n+1)
    for i in range(n):
        graph[last_year[i]]=last_year[i+1:]
        for j in graph[last_year[i]]:
            inDegree[j] += 1
            # print(f'(i, j) = {i}, {j}')
    
    c = int(input())
    changed = deque()
    for _ in range(c):
        a, b = map(int, input().split())
        changed.append((a, b))

    while changed:
        a, b = changed.popleft()
        for k in graph[a]:
            if k == b:
                graph[a].remove(b)
                inDegree[b] -= 1
                graph[b].append(a)
                inDegree[a] += 1
            else:
                graph[b].remove(a)
                inDegree[b] -= 1
                graph[a].append(b)
                inDegree[a] += 1
        
    for j in range(1, n+1):
        if inDegree[j] == 0:
            ##포기

