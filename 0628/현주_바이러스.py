import sys
input = sys.stdin.readline
from collections import deque

def main():
    N = int(input())
    C = int(input())
    graph = [[]for _ in range (N+1)]
    for _ in range(C):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (N+1)

    def bfs(v):
        infected = 0
        q = deque()
        q.append(v)
        visited[v] = True #포인트
        while q:
            x = q.popleft()
            for i in graph[x]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    infected += 1
        return infected

    answer = bfs(1)
    print(answer)

main()