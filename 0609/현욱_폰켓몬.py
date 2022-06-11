from collections import Counter

def solution(nums):
    count = int(len(nums) / 2)
    s = Counter(nums)
    # print(min(len(s),count))
    return min(len(s),count)

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])