def solution(nums):
    from collections import Counter; n = len(nums) // 2;s = Counter(nums);return min(len(s),n)
