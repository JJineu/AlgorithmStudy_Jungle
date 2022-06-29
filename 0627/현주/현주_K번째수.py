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
        
    # answer = 0
    if temp >= k: #temp>k인데 mid가 하나만 작아져도 temp<k 될수도 있음. (B[k-1], B[k], B[k+1] 등등이 다 같은 값이고 이것보다 작은게 k-1개쯤일 때.)
        answer = mid
        right = mid - 1
    else:
        # answr = mid
        left = mid + 1
    #element<=B[k]가 k개 일때 B[k] 구해야 함
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