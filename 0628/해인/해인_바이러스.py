import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
net = [[] for _ in range(n+1)] # 0번 컴퓨터와 n개의 컴퓨터 만듦
visited = [0 for _ in range(n+1)] 

for i in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]] 

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력
cnt = 0
def dfs(start):
    global cnt
    visited[start] = 1
    cnt += 1
    for i in net[start]:
        if not visited[i]: # i를 방문한 적이 없었다면
            dfs(i)

dfs(1)
print(cnt-1) # 1번 자기 자신을 제외하고 바이러스 감염되는 컴퓨터 수
