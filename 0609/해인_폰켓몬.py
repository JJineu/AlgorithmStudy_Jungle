# N마리 중 N/2마리를 가져가도 좋음
# 폰켓몬 종류 수의 최댓값은 2
# N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택 -> 폰켓몬 종류 번호의 개수
def solution(nums):
    num = dict()
    for i in nums:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    # {3: 2, 1: 1, 2: 1}
    
    answer = 0
    cnt = 0
    for k in num:
        if num[k] >= 1:
            num[k] -= 1
            cnt += 1
        else:
            continue
        if cnt == len(nums)//2:
            break
        
        
    return cnt

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])