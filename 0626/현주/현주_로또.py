import sys
input = sys.stdin.readline
from itertools import combinations

# buffers = []
while True:
    buf = input().rstrip() #rstrip 꼭 하기!!!
    if buf == '0':
        break
    else:
        nums = list(buf.split())
        n = nums[0]
        nums = nums[1:]
        # buffers.append(nums)
        for c in combinations(nums, 6):
            print(' '.join(list(map(str, c))))
        print()
  
  