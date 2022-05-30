import sys
input = sys.stdin.readline

def solution(s):
    nums = list(map(int, s.split()))
    nums.sort()
    ans = [nums[0], nums[-1]]
    
    # print(' '.join(list(map(str, ans))))
    return ' '.join(list(map(str, ans)))

# solution("1 2 3 5")
# solution("-3 -2 1 5")
