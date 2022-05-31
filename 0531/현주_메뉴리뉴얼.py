#풀다말았음
import sys
from collections import Counter
from itertools import combinations

input = sys.stdin.readline 

def solution(orders, course):
    order_history = []
    for i in orders:
        order_history.append(list(i)) #각 주문을 한 글자씩 쪼개기
    print(order_history)

    course.sort()
    order_combi = []
    answer = []
    for i in course:
        for j in order_history: #주문했던 각 조합에 대해서
            order_combi.append(sorted(combinations(j, i))) #주문했던 조합에서 i개짜리 조합 찾기
        print(order_combi)
        # order_count = Counter(order_combi)
    #     print(order_count)
    #     # [print(x) for x in order_count]

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    # answer = []
    # return answer