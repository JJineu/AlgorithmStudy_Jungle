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

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) # 1