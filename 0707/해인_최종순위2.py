# 1번 ~ n번
# 상대 순위가 바뀐 팀의 목록만 발표
# 올해 최종 순위?
# 확실한 올해 순위를 만들 수 없는 경우, 일관성이 없는 잘못된 정보
from pickle import TRUE
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    n = int(input()) # 팀의 수 n
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    queue = deque()
    answer = []
    flag = 0

    team = list(map(int, input().split()))

    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            indegree[team[k]] += 1
    
    m = int(input())

    for j in range(m):
        first, second = map(int, input().split())
        flag = True

        for k in graph[first]:
            if k == second:
                graph[first].remove(second)
                indegree[second] -= 1
                graph[second].append(first)
                indegree[first] += 1
                flag = False
        
        if flag:
            graph[second].remove(first)
            indegree[first] -= 1
            graph[first].append(second)
            indegree[second] += 1

    for j in range(1, n+1):
        if indegree[j] == 0:
            queue.append(j)
    
    if not queue:
        print("IMPOSSIBLE")
        continue

    result = TRUE
    while queue:
        if len(queue) > 1:
            result = False
            break
        tmp = queue.popleft()
        answer.append(tmp)
        for j in graph[tmp]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
            elif indegree[j] < 0:
                result = False
                break
                    

if not result or len(answer) < n:
    print("IMPOSSIBLE")
else:
    print(*answer)