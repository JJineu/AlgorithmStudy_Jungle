from sys import stdin         
input = stdin.readline
from collections import deque

def main():
    n, m = map(int, input().split())
    colors = [list(input().rstrip()) for _ in range(m)]
    
    queue = deque()
    visit = [[0 for _ in range(n)] for _ in range(m)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    friendly = 0
    enemy = 0
    for i in range(m):
        for j in range(n):
            if not visit[i][j]:
                queue.append((i, j)) # x, y
                tmp = 1
                visit[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < m and 0 <= ny < n:
                            print(f'i:{i}, j:{j}, x:{x}, y:{y}, nx:{nx}, ny:{ny}')
                            if not visit[nx][ny] and colors[i][j] == colors[nx][ny]:
                                queue.append((nx, ny))
                                visit[nx][ny] = 1
                                tmp += 1
                if colors[i][j] == 'W':
                    friendly += tmp ** 2
                else:
                    enemy += tmp ** 2
                print(f'fri:{friendly}, ene:{enemy}\n')
                    
    print(friendly, enemy)

main()