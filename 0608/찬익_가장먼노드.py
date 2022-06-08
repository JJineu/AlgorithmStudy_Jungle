# given
# 가장 멀리 떨어진 노드 = 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드
# 노드의 개수 n
# 간선 정보 2차원 배열 vertex

# solve
# 특정 노드 부터 시작 -> 1부터 시작
# 노드에서 이어진 곳이 없다면 탐색 종료
# 더 짧은 경로가 있다면 어떻게 갱신할 것인가?
# 최단 경로 이동 먼저 구현해보자 
# 예를 들어 1-2-4, 1-2-3-4에서 1-2-4가 가장 먼 노드로 어떻게 판단?
# -> 다익스트라 단방향에서 양방향으로
    
import sys
from heapq import heappop, heappush
inf = sys.maxsize

def dijkstra(start):
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


def solution(n,edge):
    global graph
    graph = [[] for _ in range(n+1)]
    
    global dp
    dp = [inf] * (n+1)
    
    global heap
    heap = []
    
    for a,b in edge:
        graph[a].append([b,1])
        graph[b].append([a,1])

    dijkstra(1)
    arr = []
    cnt = 0
    
    for i in dp:
        if i != inf:
            arr.append(i)
    for j in arr:
        if j == max(arr):
            cnt += 1
    
    return cnt