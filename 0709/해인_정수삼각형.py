import sys
input = sys.stdin.readline

n = int(input())
tri = [[] for _ in range(n)]
dp = [[] for _ in range(n)]

for i in range(n):
    tri[i] = [0] + list(map(int, input().split())) + [0]
    dp[i] = [0 for _ in range(i+3)]

# [[0, 7, 0], [0, 3, 8, 0], [0, 8, 1, 0, 0], [0, 2, 7, 4, 4, 0], [0, 4, 5, 2, 6, 5, 0]]  

dp[0][1] = tri[0][1]

for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

tmp = []
for i in dp[n-1]:
    tmp.append(i)

print(max(tmp))