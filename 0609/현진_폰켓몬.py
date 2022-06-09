# 배열길이의 반절 선택, 가장 많은 종류

from collections import Counter

def solution(nums):
    n = int(len(nums) / 2)
    s = Counter(nums)
    # print(s)
    # print(min(len(s),n))
    return min(len(s),n)

solution([3,1,2,3])
solution([3,3,3,2,2,4])
