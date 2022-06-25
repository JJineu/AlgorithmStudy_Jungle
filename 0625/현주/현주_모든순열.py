import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
nums = [i for i in range(1, N+1)]
perms = list(permutations(nums, N))

for p in perms:
    print(' '.join(list(map(str, p))))