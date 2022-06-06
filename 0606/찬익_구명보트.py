# 보트 최대 2명
# 사람들의 몸무게를 담은 배열 people
# 무게 제한 limit
# 모든 사람 구출을 위한 구명보트의 최솟값 return

def solution(people, limit):
    people = sorted(people)
    cnt = 0
    i = 0
    j = len(people) - 1
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        cnt += 1
    return cnt