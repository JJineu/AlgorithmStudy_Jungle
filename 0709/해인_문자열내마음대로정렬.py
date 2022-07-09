# 풀이 1
def solution(strings, n):
    word = dict()
    tmp = []
    
    for i in range(len(strings)):
        c = strings[i][n]
        if c not in tmp:
            tmp.append(c)

    tmp = sorted(tmp)
    for i in tmp:
        word[i] = []
    
    strings = sorted(strings)
    
    for i in range(len(strings)):
        word[strings[i][n]] += [strings[i]]
    
    answer = []
    
    for i in word.keys():
        for j in word[i]:
            answer.append(j)
    
    return answer

# 풀이 2
def solution(strings, n):
    strings = sorted(strings)
    return sorted(strings, key = lambda x:(x[n]))