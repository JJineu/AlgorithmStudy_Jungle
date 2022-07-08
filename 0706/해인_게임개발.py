from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
build = [[] for _ in range(n+1)] # n개 빌딩별 연결 빌딩
time = [0 for _ in range(n+1)] # 빌딩 n이 지어지는 데 걸리는 시간
conn = [0 for _ in range(n+1)] # 빌딩 n의 진입 차수

for i in range(1, n+1):
    tmp = list(map(int, input().split()))[:-1]
    time[i] = tmp[0] # 지어지는 데 걸리는 시간
    building_data = tmp[1:]

    # 간선 연결 및 진입차수 설정
    for j in building_data:
        conn[i] += 1
        build[j].append(i) 
        # 나를 연결되어 있는 빌딩의 인덱스에 넣어줌 (단방향이므로 하나만 넣어주면 됨)
        # 먼저 지어져야 하는 건물들의 번호 추가

def topology_sort():
    result = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if conn[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result[now] += time[now]
        for b in build[now]:
            conn[b] -= 1
            result[b] = max(result[b], result[now])
            if conn[b] == 0:
                q.append(b)
                
    return result


answer = topology_sort()
for i in range(1, n+1):
    print(answer[i])