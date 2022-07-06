import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)
time = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))[:-1]
    time[i] = data[0]
    graph_data = data[1:]

    #미리 지어져야할 건물들의 graph에 나중에 지어질 건물 입력
    #우리가 익숙한 먼저->나중 순서로 graph 배열 정리하는 것임
    for j in graph_data:
        graph[j].append(i)
        inDegree[i] += 1

def topology_sort():
    result = [0] * (N+1) #각 건물 다 짓는데 걸리는 시간
    q = deque()

    #inDegree가 없는(미리 지어져야 하는 건물이 없는) 애들부터 q에 넣는다.
    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result[now] += time[now] #이제 내가 지어진다 (그전까지 시작x, pre짓는데 걸리는 시간만 계산한 것)
        for b in graph[now]:
            result[b] = max(result[b], result[now]) #업데이트
            inDegree[b] -= 1 #prerequisite 중 하나 다 지어졌다
            if inDegree[b] == 0:
                q.append(b)

    [print(x) for x in result[1:]]
    return

topology_sort()