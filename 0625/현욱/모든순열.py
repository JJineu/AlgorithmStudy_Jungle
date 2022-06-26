import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = [i for i in range(1, N+1)]
nPr = list(permutations(nums, N))
nPr.sort()

for P in nPr:
    print(' '.join(list(map(str, P))))