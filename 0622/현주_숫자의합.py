import sys
input = sys.stdin.readline

N = int(input())
# answer = 0
nums = map(int, list(input().rstrip()))
answer = sum(nums)
print(answer)