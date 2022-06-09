def solution(nums):
    answer = 0
    n = len(nums) // 2
    numbers = set(nums)
    if len(numbers) >= n:
        print(n)
        return n
    else:
        print(len(numbers))
        return len(numbers)

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])