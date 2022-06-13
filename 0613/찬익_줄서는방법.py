# n명 -> 1 ~ n
# 사람이 줄 설 수 있는 경우의 수
# permutation

# 효율성 fail
# 정답은 통과
from itertools import permutations

def solution(n, k):
    arr = []
    people = []
    for i in range(1,n+1):
        people.append(i)
    
    arr = list(permutations(people, n))
    
    return arr[k-1]

# ---
# 시간초과
from itertools import permutations
import math
def solution(n, k):
    arr = []
    people = []
    for i in range(1,n+1):
        people.append(i)
    
    p = math.factorial(n)
    
    if n != p:
        arr = list(permutations(people, n))
        return arr[k-1] 

    else :
        ans = []
        for i in people:
            ans.append(people[-1])
        return ans

# --- 
# 구현 중간 백업
# 직접 배치하여 하나의 값만 찾는 방법으로
# 맨 앞자리
# 전체 케이스에서 all_case/len(n) 한 경우만큼 할당됨
# 예를 들어 123은 케이스 6가지, 1이 앞자리인 경우는 6/3 = 2
# 따라서 이런 순서로 내려가는 방법으로 구현

# 두번째 수는
# 첫번째 수를 스택에서 제외한 다음
# 남은 순서대로 하나씩 돌림
# 앞자리 n개를 선택하고 남은 n-1 가지 경우의 수 

# 이런 순서대로 stack에 있는 모든수가 사라질 때마다 cnt += 1

import math

def solution(n, k):
    
    step = math.factorial(n)
    bucket = step // n
    idx = k // bucket
    key = step % k
        
    ans = []
    for i in range(1, n+1):
        ans.append(i)
        
    # answer = []
    # answer.append(ans[bucket])
    # answer.append(ans[key-1])
    # answer.append(ans[idx-1])
    return answer
# ---
# 통과
# 직접 배치하여 하나의 값만 찾는 방법으로
# 맨 앞자리
# 전체 케이스에서 all_case/len(n) 한 경우만큼 할당됨
# 예를 들어 123은 케이스 6가지, 1이 앞자리인 경우는 6/3 = 2
# 따라서 이런 순서로 내려가는 방법으로 구현

# 두번째 수는
# 첫번째 수를 스택에서 제외한 다음
# 남은 순서대로 하나씩 돌림
# 앞자리 n개를 선택하고 남은 n-1 가지 경우의 수 

# 이런 순서대로 stack에 있는 모든수가 사라질 때마다 cnt += 1

import math

def solution(n, k):
    ans = []
    answer = []
    for i in range(1, n+1):
        ans.append(i)
    
    while(n != 0):
        step = math.factorial(n)
        bucket = step // n
        idx = k // bucket
        k = k % bucket

        if k == 0:
            answer.append(ans.pop(idx-1))
        else :
             answer.append(ans.pop(idx))

        n -= 1

    return answer