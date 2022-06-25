import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrC = sorted(arrA + arrB)
print(' '.join(list(map(str, arrC))))


# answer = []
# while arrA and arrB:
#     if arrA[0] < arrB[0]:
#         answer.append(arrA.pop(0))
#     elif arrA[0] > arrB[0]:
#         answer.append(arrB.pop(0))
#     else: #when arrA[0] == arrB[0]
#         answer.append(arrA.pop(0))
#         answer.append(arrB.pop(0))
        
# if arrA:
#     for i in arrA:
#         answer.append(i)
# elif arrB:
#     for j in arrB:
#         answer.append(j)

# print(' '.join(list(map(str, answer))))