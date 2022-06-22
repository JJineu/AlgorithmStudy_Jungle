import sys
input = sys.stdin.readline

N = int(input()) # 1
data = list(input().rstrip())
result = 0
for i in data :
  result += int(i)
print(result)
