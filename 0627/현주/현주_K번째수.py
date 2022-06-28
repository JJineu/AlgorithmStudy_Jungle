import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

left = 1
right = N**2

while left <= right:
    mid = (left+right)//2

    #행별로 우리가 찾는 mid보다 작은 숫자의 개수 세기
    temp = 0
    for i in range(1, N+1): 
        temp += min(mid//i, N)
    print(f'{mid}, {temp}')
    answer = 0
    if temp > k:
        right = mid - 1
    elif temp < k:
        left = mid + 1
    else: #왜 temp == k가 없음? 그리고 왜 답을 temp<=k일 때로 주면 안되고 temp>=k여야 됨?
        answer = mid

print(answer)




'''메모리초과 풀이'''
# arrA = [[] for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         arrA[i].append(i*j)

# arrB = []
# for i in arrA:
#     if i:
#         for elems in i:
#             arrB.append(elems)
# arrB.sort()
# print(arrB[k-1])