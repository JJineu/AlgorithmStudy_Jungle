#풀다말았음
import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline 

def solution(orders, course):
    combList = []
    for order in orders:
        order = sorted(order)
        for c in course:
            combList += combinations(order, c)
        # print(combList)

    cnt = Counter(combList).most_common() #(('A', 'C'), 4), key = ('A', 'C'), value = 4
    answer, resMap = [], {}
    for key, value in cnt: #생성된 모든 조합에 대해
        #len(key) 길이의 조합 중 제일 큰 게 value번 나왔어 (즉 2개짜리 조합 하나가 4번 주문됐다고 저장했는데 2개짜리조합 4주문이 하나 더 나온 거임)
        #이 개수조합으로 제일 많이 occur한 조합이 가장 먼저 입력됨
        if len(key) not in resMap.keys() or resMap[len(key)] == value:
            if value <= 1: break
            resMap[len(key)] = value 
            answer.append(''.join(key))
            # print(f'resMap = {resMap}')
    # print(sorted(answer))
    return sorted(answer)
    
    
    '''내 풀이'''
    # order_history = []
    # for i in orders:
    #     order_history.append(list(i)) #각 주문을 한 글자씩 쪼개기
    # print(order_history)

    # course.sort()
    # order_combi = []
    # answer = []
    # for i in course: #메뉴 2개짜리, 3개짜리, 4개짜리
    #     for j in order_history: #주문했던 각 조합에 대해서
    #         order_combi.append(sorted(combinations(j, i))) #주문했던 조합에서 i개짜리 조합 찾기
    #     order_count = Counter(tuple(order_combi))


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    # answer = []
    # return answer