import sys
input = sys.stdin.readline

def solution(brown, yellow):
    answer = []
    s = brown + yellow

    lst = []
    for i in range(1, s+1):
        if s % i == 0:
            lst.append((i, s//i))        

    while lst:
        x, y = lst.pop()
        if (x-2) * (y-2) == yellow:
            #print([x,y])
            #break
            return [x,y]

solution(10, 2) # 4, 3
solution(8, 1) # 3, 3
solution(24, 24) # 8, 6