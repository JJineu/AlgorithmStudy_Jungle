import sys
input = sys.stdin.readline

# K개의 랜선, N개 만들고자 함
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함

n, k = map(int, input().split())
lensun = []
for i in range(n):
    lensun.append(int(input()))
lensun = sorted(lensun)

start = 1
end = lensun[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lensun:
        cnt += i // mid
    if cnt >= k: # cnt가 너무 크면 mid를 크게 해야
        answer = mid
        start = mid + 1
    else: # cnt가 너무 작으면 mid를 작게 해야
        end = mid - 1

print(answer)