import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
# print(graph)
dp = [[0] * N for _ in range(N)]
dp[0][0] = graph[0][0]

def triangle(x, y):
    # print(f'x, y = {x, y}')
    if dp[x][y] != 0:
        return dp[x][y]
    
    if x > 0:
        if y == 0:
            dp[x][y] = triangle(x-1, y) + graph[x][y]
        elif y == x:
            dp[x][y] = triangle(x-1, y-1) + graph[x][y]
        else:
            dp[x][y] = max(triangle(x-1, y-1), triangle(x-1, y)) + graph[x][y]

    return dp[x][y]

for i in range(N):
    triangle(N-1, i)
print(max(dp[N-1]))
