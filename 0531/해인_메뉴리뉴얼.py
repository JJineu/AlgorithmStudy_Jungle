# # 내가 풀어본 풀이
# def solution(orders, course):
#     dic = {}
#     for ind, i in enumerate(orders):
#         for j in range(len(i)):
#             if i[j] not in dic:
#                 dic[i[j]] = {ind+1}
#             else:
#                 dic[i[j]] = dic[i[j]].union({ind+1})
    
#    	# {'A': {1, 2, 4, 6}, 'B': {1, 5}, 'C': {1, 2, 3, 4, 5, 6}, 'F': {1, 5}, 'G': {1, 5}, 'D': {3, 4, 6}, 'E': {3, 4, 6}, 'H': {6}}
#     # {'A': {1, 2, 4, 7}, 'B': {1, 2}, 'C': {1, 3, 7}, 'D': {1, 3, 4, 7}, 'E': {1, 4}, 'X': {5, 6}, 'Y': {5, 6}, 'Z': {5, 6}}
    
#     print(dic)
    
#     answer = []
#     return answer


# 찾아본 답안 (이해 아직 못함)
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k): # 각 사람 당 주문한 단품 메뉴 중 원하는 코스 요리 개수 개의 조합을 구함
                # menu_li ACDEH : 한 사람이 ACDEH 메뉴를 골랐을 때 4개의 코스 요리를 선택하는 경우의 li
                # combi ('A', 'C', 'D', 'E')
                # combi ('A', 'C', 'D', 'H')
                # combi ('A', 'C', 'E', 'H')
                # combi ('A', 'D', 'E', 'H')
                # combi ('C', 'D', 'E', 'H')
                res = ''.join(sorted(li)) # 해당 조합을 문자열로 만들기, 오름차순 정렬
                candidates.append(res) # 조합을 candidates라는 후보자에 넣음
        print(candidates, Counter(candidates))
        # ['AB', 'AC', 'AF', 'AG', 'BC', 'BF', 'BG', 'CF', 'CG', 'FG', 'AC', 'CD', 'CE', 'DE', 'AC', 'AD', 'AE', 'CD', 
        # 'CE', 'DE', 'BC', 'BF', 'BG', 'CF', 'CG', 'FG', 'AC', 'AD', 'AE', 'AH', 'CD', 'CE', 'CH', 'DE', 'DH', 'EH'] Counter({'AC': 4, 'CD': 3, 'CE': 3, 'DE': 3, 'BC': 2, 'BF': 2, 'BG': 2, 'CF': 2, 'CG': 2, 'FG': 2, 'AD': 2, 'AE': 2, 'AB': 1, 'AF': 1, 'AG': 1, 'AH': 1, 'CH': 1, 'DH': 1, 'EH': 1})
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)  

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

solution(orders, course)