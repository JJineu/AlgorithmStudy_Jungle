import heapq

def solution(A,B):
    
    A.sort()
    B.sort()
    L = len(A)
    sum = 0

    for i in range(L):
        sum += A[i] * B[-i-1]

    # print(sum)
    return(sum)

# solution([1, 2], [3, 4])

 # max = sys.max

    # arr = [max] * (L+1)
    # visitedB = [False] * (L+1)

    # for i in range(L):
    #     for j in range(L):
    #         visitedB[j] = 1
    #         if A[i] * B[j] < arr[i]:
    #             arr[i] = A[i] * B[j]
    #         else:
    #             visitedB[j] = 0
        
    # print(sum)
    # return(sum)
                # if i*j < min:
                #     min = i*j