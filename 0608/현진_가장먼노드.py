# 1에서 시작하여 모든 노드까지(도착지점)까지의 거리 계산
# 종료조건? 1로 돌아왔을 때, visit 지점 왔을 때

from collections import deque

def solution(n, edge):
    answer = 0

    # 각 인덱스와 연결된 노드 넣기
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # visit 으로 방문여부 1번 노드와의 거리 구할 것
    visit = [0] * (n+1)
    visit[1] = 1
    q = deque([1])

    while q:
        x = q.popleft()
        for i in graph[x]: # x 노드와 연결된 노드 찾아서 거리계산
            if not visit[i]:
                visit[i] += visit[x] + 1
                q.append(i)

    max_c = max(visit)

    for i in visit:
        if i == max_c:
            answer += 1

    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
