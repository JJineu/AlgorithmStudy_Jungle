import sys
input = sys.stdin.readline

a, b = map(int,input().split())
list_A = list(map(str,input().split()))
list_B = list(map(str,input().split()))

# 되는 코드
list_R = list_A + list_B
list_R.sort()
print(*list_R)

# 안되는 코드
# str -> int 로 배열내의 타입을 변경하는 과정에서 문제가 있는건가?
# list_R = list(set(list_A) | set(list_B))
# list_R = list(map(int, list_R))
# list_R.sort()
# print(*list_R)


