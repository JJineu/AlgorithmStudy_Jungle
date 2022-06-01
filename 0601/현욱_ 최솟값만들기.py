# 테스트케이스 통과 - 효율성 통과 X
def solution(A,B):
    result = 0
    for i in range(len(A)) :
        minA = min(A)
        maxB = max(B)
        A.remove(maxB)
        B.remove(maxB)
        result += i * maxB
    answer = result

    return answer

# 정답
def solution(A,B):
    result = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)) :
        result += (A[i] * B[i])
    answer = result

    return answer