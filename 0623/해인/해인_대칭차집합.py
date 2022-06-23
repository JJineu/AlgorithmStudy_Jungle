import sys
input = sys.stdin.readline
a, b = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))

# 풀이 1 (시간 짧게 소요됨)
# total = len(setA + setB)
# minus = len(set(setA + setB))

# answer = total - 2*(total-minus)

# print(answer)

# 풀이 2
# 집합의 연산 (차집합)
setA = set(setA)
setB = set(setB)

answer = len(setA - setB) + len(setB - setA)
print(answer)

# 교집합 연산 &
# 차집합 연산 -
# 합집합 연산 + 