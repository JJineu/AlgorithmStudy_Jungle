from itertools import combinations

# 성공
def solution(orders, course):
    answer = []
    count = [{} for _ in range(11)] # 2 ~ 10개, 0-1 사용안함

    for order in orders:
        tmps = [] 
        for i in range(2, len(order)+1):
            tmps = list(combinations(order,i))
            for tmp in tmps:
                t = ''.join(sorted(tmp))
                if t not in count[len(t)]:
                    count[len(t)][t] = 1
                else:
                    count[len(t)][t] += 1
    for i in range(2, 11):
        count[i] = sorted(count[i].items(), key = lambda x:x[1], reverse = True)
    
    # for tttt in count:
    #     print(tttt)

    for co in course:
        if not count[co]:
            continue

        val = count[co][0][1]
        if val > 1:
            answer.append(count[co][0][0])
        else:
            continue

        idx = 1
        while 1:
            # print(f'co: {co}, idx: {idx}')
            try:
                if count[co][idx][1] == val:
                    answer.append(count[co][idx][0])
                    idx += 1
                else:
                    break
            except:
                break
    
    return sorted(answer)
    # print(sorted(answer))

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
# solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
# solution(["XYZ", "XWY", "WXA"], [2,3,4])