def solution(s):
    answer = []
    data = []
    for s in s[2:-2].split('},{') :
        data.append(s.split(','))
        # print('정렬전',data)
    data.sort(key=len)
    # print('정렬후',data)
    for i in data :
        for j in i :
            if int(j) not in answer:
                answer.append(int(j))
                break
    return answer