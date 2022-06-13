#시간초과
from itertools import permutations

def solution(n, k):
    answer = []
    people = list(range(1,n+1))
    s = []
    # s = permutations(people,n)
    cnt = 0
    for i in permutations(people,n):
        cnt += 1
        if cnt == k:
            for j in range(n):
                answer.append(i[j])
            # answer = i
    # answer = s[k]
    print(answer)
    return answer
solution(3,5)


# 첫번째 수 정해지면 경우의수-> (n-1)!
# 두번째 수 정해지면 경우의수-> (n-2)!
# (n-1)!이 n 개 나열되어 있는 형태
# k번째는 k%n == 0 -> k//n 그룹
# k%n != 0 -> k//n +1 그룹 
