# An(맨위)의 최댓값은 A(n-1) 왼쪽 오른쪽 중 큰 값
# d[n] = max(d1[n-1], d2[n-1]) + a[n]
## re
# triangle[1][0] + triangle[0][0], triangle[1][1]+ triangle[0][0]
# triangle[1][0] + triangle[2][0], triangle[1][0] + triangle[2][1]
# triangle[1][1] + triangle[2][1], triangle[1][1] + triangle[2][2]
## re
# 맨왼쪽 맨오른쪽은 경우의 수 1개
# 1번과 n-1번은 왼쪽 1개 오른쪽 여러개
# 2번과 n-2번은 왼쪽의 왼쪽 1개, 왼쪽의 오른쪽?, 오른쪽의 오른쪽 1개, 오른쪽의 왼쪽??

# 일단은 71점

def solution(triangle):
    answer = 0
    n = len(triangle)
    # 0번째
    sum = 0
    for i in range(n):
        sum += triangle[i][0]
    # n번째
    sum2 = 0
    for i in range(n):
        sum2 += triangle[i][i]
    # 1-n-1
    for i in range(n):
        for j in range(0,i):
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
            # print(triangle[i][j])
    # for i in range(n):
    # a = max(triangle[n])
    a = max(triangle[n-1])
    # print(a)
    # print(a)
    answer = max(sum, sum2, a)
    # print(a)
    return answer