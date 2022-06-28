import sys
input = sys.stdin.readline

# 나 : 흰(W) / 적 : 파(B)
# N명 : N 제곱의 위력

n, m = map(int, input().split()) # n:열, m:행
vone = [[0 for _ in range(n)] for _ in range(m)] 
vtwo = [[0 for _ in range(n)] for _ in range(m)]
war = [list(input().rstrip()) for _ in range(m)]

# [['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], 
#  ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'W', 'W'],
#  ['W', 'W', 'W', 'W', 'W']]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wcnt = 0
bcnt = 0
def dfs(x, y): # x:행, y:열
    global wcnt
    vone[x][y] = 1
    wcnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1 and war[nx][ny] == 'W':
            if vone[nx][ny] == 0:
                dfs(nx, ny)

def dfsblue(x, y): # x:행, y:열
    global bcnt
    vtwo[x][y] = 1
    bcnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= m-1 and 0 <= ny <= n-1 and war[nx][ny] == 'B':
            if vtwo[nx][ny] == 0:
                dfsblue(nx, ny)

wfinal = 0
for i in range(m): # i:행
    for j in range(n): # j:열
        if not vone[i][j] and war[i][j] == 'W': # W이고 방문한 적 없다면 dfs를 돌음
            dfs(i, j)
            wfinal += wcnt**2
            wcnt = 0

bfinal = 0
for i in range(m): # i:행
    for j in range(n): # j:열
        if not vtwo[i][j] and war[i][j] == 'B': # W이고 방문한 적 없다면 dfs를 돌음
            dfsblue(i, j)
            bfinal += bcnt**2
            bcnt = 0

print(wfinal, bfinal)


