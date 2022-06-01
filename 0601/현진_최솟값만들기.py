# 시간초과
def solution(A,B):
    answer = 0

    A.sort() # sort 뒤에 () 할 것
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i]*B[i]
            
    return answer

# 정답코드 
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)

    answer = sum([a * b for a, b in zip(A, B)])
    return answer