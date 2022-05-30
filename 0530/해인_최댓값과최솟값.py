def solution(s):
    num = sorted(list(map(int, s.split())))
    
    answer = str(num[0]) + " " + str(num[len(num)-1])
    return answer