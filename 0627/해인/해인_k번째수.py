import sys
input = sys.stdin.readline

n = int(input())
k = int(input()) # 인덱스로 k-1인 수를 출력해줘야
B = []

for i in range(n): # 0, 1, 2
    for j in range(n): # 0, 1, 2  
        B.append((i+1)*(j+1))

B = sorted(B)

def bsearch(t):
    start = 0
    end = len(B)-1
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        if mid < t:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    return B[ans]

print(bsearch(k-1))
