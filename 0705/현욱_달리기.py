import sys
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = []
visited = [[0] * M for i in range(N)]
for i in range(N):
    matrix.append(list(input().rstrip()))


print(matrix)
print(visited)
