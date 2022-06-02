# 22분 소요
def solution(s):
    nlist = s.split("},{")
    nlist[0] = nlist[0][2:]
    nlist[len(nlist)-1] = nlist[len(nlist)-1][:-2]
    
    # nlist ['2', '2,1', '2,1,3', '2,1,3,4']
    slist = []
    for num in nlist:
        slist.append(list(map(int, num.split(','))))
    # slist [[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]
    
    # 원소의 개수 순으로 slist 정렬
    slist.sort(key=lambda x: (len(x)))
    # slist [[2], [2, 1], [1, 2, 3], [1, 2, 4, 3]]
    
    answer = [slist[0][0]]
    
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            if slist[i][j] in answer:
                continue
            if slist[i][j] not in answer:
                answer.append(slist[i][j])
    print(answer)
    
    return answer