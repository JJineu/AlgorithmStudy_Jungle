def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x: x[n])
    return strings

# lambda 하기 전에 sort를 해주는 것이 포인트.