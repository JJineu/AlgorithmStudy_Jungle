import sys
input = sys.stdin.readline


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


N = int(input())
count = int(input())

graph = [[] for i in range(N + 1)]

for _ in range(count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

dfs(1)

result = -1

for j in range(1, len(visited)):
    if visited[j] == True:
        result = result + 1

print(result)
