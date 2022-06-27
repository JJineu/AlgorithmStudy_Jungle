import sys
input = sys.stdin.readline

N, M = map(int, input().split())
classes = list(map(int, input().split()))

left = 0
right = sum(classes)

while left <= right:
    mid = (left + right)//2 #블루레이의 길이

    bluerays = 1
    duration = 0
    for i in classes:
        if (duration + i) > mid:
            bluerays += 1 #새로운 블루레이에 기록
            duration = i
        else:
            duration += i
    
    if bluerays > M: #한 블루레이에 더 많이 담아야 됨
        left = mid + 1
    else: #bluerays <= M
        answer = mid
        right = mid - 1

print(answer)