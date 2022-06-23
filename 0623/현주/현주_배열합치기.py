import sys
input = sys.stdin.readline
import heapq
from heapq import heappush, heappop

N, M = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

answer = []
while arrA and arrB:
    if arrA[0] < arrB[0]:
        answer.append(heappop(arrA))
    else: #arrA[0] > arrB[0]
        answer.append(heappop(arrB))
        
if arrA:
    for i in arrA:
        answer.append(i)
else:
    for i in arrB:
        answer.append(i)

print(*answer, sep = ' ')