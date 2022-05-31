# 절대 정답 아님
# 가장 많이 주문된 개별 메뉴 순서로 조합을 짜버림

import sys
from itertools import combinations
input = sys.stdin.readline

def solution(orders, course):
    count = [0 for _ in range(26)] # A, B, C, ..., Z
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for order in orders:
        for c in order:
            count[ord(c) - 65] += 1

    alphabet_count = [(count[x], alphabet[x]) for x in range(26)]
    alphabet_count.sort(reverse=True)
    # print(alphabet_count)    

    ans = []
    for cnt in course:
        tmp = alphabet_count[cnt-1][0] # 마지막 놈이 팔린 갯수
        start = cnt # 마지막 놈과 같은 개수만큼 팔린 것의 시작 idx
        end = cnt
        
        # 시작 idx 찾기
        for i in range(cnt-1, -1, -1):
            if alphabet_count[i][0] == tmp:
                start = i
            else:
                break
        
        # 끝 idx 찾기
        for i in range(cnt-1, 26):
            if alphabet_count[i][0] == tmp:
                end = i
            else:
                break

        # print(alphabet_count)
        # print(f'tmp: {tmp}, start: {start}, end: {end}')

        # 이제 조합을 만들자
        menu = ""
        for i in range(start):
            menu += alphabet_count[i][1]
            cnt -= 1

        # 이제 cnt개 더 뽑으면 된다. 모든 조합을 start ~ end 범위에서 찾자
        target_list = alphabet_count[start:end+1]
        # print(menu, cnt, target_list)

        # 조합을 저장하는 배열
        combs = list(combinations(target_list, cnt))
        
        for comb in combs:
            menu_tail = ""
            for c in comb:
                menu_tail += c[1]
            ans.append(menu + menu_tail)
            
    for i in range(len(ans)):
        ans[i] = ''.join(sorted(ans[i]))

    print(sorted(ans))
    return

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
solution(["XYZ", "XWY", "WXA"], [2,3,4])