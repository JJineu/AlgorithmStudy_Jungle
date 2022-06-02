import sys

def solution(s):
    slist = s[2:-2].split('},{')
    
    data = []
    for i in slist:
        data.append(i.split(','))
    #여기서 sort해줘야 요소개수별로 sort됨!!
    #미리 하면 세자릿수가 더 요소 많은 애처럼 됨...
    data = sorted(data, key = len) 
    # print(data)

    answer = []
    for i in data:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
    

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")