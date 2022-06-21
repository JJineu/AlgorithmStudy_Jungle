# 틀린 풀이
def solution(words):

    tmp = []
    mid = [[] for _ in range(len(words))]
    cnt = 0

    # for i in range(len(words)): # 4 -> 0,1,2,3
    #     tmp = words[:i] + words[i+1:] # 자기 자신을 제외한 대기 리스트 3 -> 0,1,2
    
    for i in range(len(words)):    
        for j in range(len(words[i])):
            mid[i].append(words[i][:j+1])
    # [['g', 'go'], ['g', 'go', 'gon', 'gone'], ['g', 'gu', 'gui', 'guil', 'guild']]
    
    for i in range(len(mid)):
        for k in range(len(mid[i])):
            print(mid[i][k])
            for j in range(len(words)): # 4 -> 0,1,2,3
                tmp = words[:j] + words[j+1:]
        
    answer = 0
    return answer
