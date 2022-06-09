import sys
input = sys.stdin.readline
from itertools import combinations

'''시간초과'''

def solution(nums):

    combis = list(combinations(nums, len(nums)//2))
    answer = 0
    for com in combis:
        cnt = len(set(com))
      
        if answer < cnt:
            answer = cnt
       
    print(answer)
    return answer
        

    # answer = 0
    # return answer

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])


        # cnt = len(com)
        # temp = []
        # for i in com:
        #     if i not in temp:
        #         temp.append(i)
        # print(temp)
  