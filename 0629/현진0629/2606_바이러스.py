# bfs

# from sys import stdin
# input = stdin.readline
# from collections import deque

# def main():
#     n = int(input())
#     e = int(input())
#     graph = [[] for _ in range(n+1)]

#     for _ in range(e):
#         a,b = map(int,input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     print(graph)
#     visit = [False]*(n+1)
#     cnt = 0

#     q = deque([1])
#     visit[1] = True
#     while q:
#         v = q.popleft()
#         for i in graph[v]:
#             if not visit[i]:
#                 visit[i] = True
#                 q.append(i)
#                 cnt += 1

#     print(cnt)

# main()




# dfs

from sys import stdin  
input = stdin.readline

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False]*(n+1)

cnt = 0
def dfs(x):
    global cnt
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)