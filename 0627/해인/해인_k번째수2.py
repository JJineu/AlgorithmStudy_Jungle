import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, n**2

while start <= end:
    mid = (start + end) // 2

    # 행별로 i*j=mid 보다 작은 숫자의 개수 세기
    tmp = 0 # mid보다 작거나 같은 숫자를 전부 구해줌
    for i in range(1, n+1):
        tmp += min(mid//i, n) # mid 이하의 i의 배수의 개수 or 최대 n
    
    if tmp >= k: # 이분탐색 실행
        answer = mid
        end = mid - 1 # tmp가 k이상이므로 mid가 작아져야 해서 end = mid - 1
    else:
        start = mid + 1

print(answer)
