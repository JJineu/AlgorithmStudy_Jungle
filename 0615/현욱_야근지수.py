# 마지막 케이스 시간초과 / 효율성은 통과함
def solution(n, works):
    count = n
    sum = 0
    maxValue = max(works)

    while count > 0 :
        for j in range(len(works)) :
            if works[j] == maxValue :
                count -= 1
                works[j] -= 1
                if works[j] < 0 :
                    works[j] = 0
            if count == 0 :
                break
        maxValue -= 1

    for k in works :
        sum += k*k

    return sum