import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, n**2
ans = 0
while start <= end:
    mid = (start + end) // 2     # i*j 값이 mid일 때
    tmp = 0
    for i in range(1, n+1):
        tmp += min(n, mid // i)  # 각 행을 돌면서 mid 이하인 수의 개수를 셈
    
    if tmp <= k:
        # print('tmp:',tmp)
        ans = mid
        start = mid + 1
    elif tmp > k:
        end = mid - 1

print(ans)
