n = int(input())
ma = [[] for _ in range(n)]
for i in range(n):
    # ma[i] = list(map(int,input().split()))
    ma[i] = [int(x) for x in input().split()]


def f(y1, x1, y2, x2, t):
    cnt = 0
    tg, tp = 0, 0
    if t == 0:
        for y in range(y1, y2):
            g, p = 0, 0
            for x in range(x1, x2):
                if ma[y][x] == 2:
                    g+=1
                elif ma[y][x] == 1:
                    p+=1
            if g == 0 and p > 0:
                cnt += f(y1, x1, y, x2, 1) * f(y+1, x1, y2, x2, 1)
            tg += g
            tp += p
    else:
        for x in range(x1, x2):
            g, p = 0, 0
            for y in range(y1, y2):
                if ma[y][x] == 2:
                    g+=1
                elif ma[y][x] == 1:
                    p+=1
            if g == 0 and p > 0:
                cnt += f(y1, x1, y2, x, 0) * f(y1, x+1, y2, x2, 0)
            tg += g
            tp += p
    if tg == 1 and tp == 0:
        return 1
    return cnt

cnt = f(0, 0, n, n, 0) + f(0, 0, n, n, 1)
if cnt == 0:
    cnt = -1
print(cnt)