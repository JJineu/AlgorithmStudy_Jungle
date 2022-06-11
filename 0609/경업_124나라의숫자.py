def solution(n):
    dic = {0:"4", 1:"1", 2:"2"}
    answer = []    
    
    while n // 3 > 0:
        tmp = n % 3
        if tmp: # 1 or 2
            answer.append(dic[tmp])
        else: # 0
            answer.append(dic[tmp])
            n -= 1

        n //= 3
    if n:
        answer.append(dic[n])
    
    # print(''.join(list(map(str,answer/
    # 
    # [::-1]))))
    return ''.join(list(map(str,answer[::-1])))

for i in range(1, 21):
    solution(i)


# 1 1
# 2 2
# 3 4
# 4 11
# 5 12
# 6 14
# 7 21
# 8 22
# 9 24
# 10 41
# 11 42
# 12 44 여기 문제있다
# 13 111
# 14 112
# 15 114