import sys
input = sys.stdin.readline

K, N = map(int, input().split())
own = []
for _ in range(K):
    own.append(int(input().rstrip()))

left = 1 #조건에 랜선의 길이는 1이상이라고 나와있어서!!!
right = max(own)

while left <= right:
    mid = (left + right)//2
    count = 0

    for i in own:
        if i >= mid:
            count += i//mid
    
    if count >= N:
        answer = mid
        left = mid + 1 #좀 더 길게 잘라도 되겠다
    else:
        right = mid - 1

print(answer)

