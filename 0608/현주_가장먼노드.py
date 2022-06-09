import sys
from collections import deque
input = sys.stdin.readline

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        a, b = edge[i][0], edge[i][1]
        graph[a].append(b)
        graph[b].append(a)

    big = sys.maxsize
    distance = [0, 0] + [big] * (n-1) #1에서 각 노드로 오는 거리 저장
    
        
    def bfs(i, count):
        q = deque([(i, count)])
        # q.append((i, count))
    
        while q:
            node, dist = q.popleft()
            for j in graph[node]:
                if distance[j] > dist:
                    distance[j] = dist
                    q.append([j, dist+1])
        # return count

    bfs(1, 1)
    biggest = max(distance)
    answer = distance.count(biggest)
    
    # print(distance.count(biggest))
    return answer
#나는 if distance를 썼기 때문에 visited 없어도 됨...    
    

    # return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])