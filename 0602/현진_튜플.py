def solution(s):
    answer = []
    # 집합 길이 순으로 나열
    # 앞에 원소 없는 것 찾아서 길이-1 인덱스에 넣기

    s1 = s.lstrip('{').rstrip('}').split('},{')
    # lstrip 왼쪽으로 { 문자열 제거, 인자가 없을 경우 왼쪽 공백 제거. 
    # rstrip 오른쪽으로 } 문자열 제거 
    # print(s1) >>> ['2', '2,1', '2,1,3', '2,1,3,4']
    
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    # print(new_s) >>> [['2'], ['2', '1'], ['2', '1', '3'], ['2', '1', '3', '4']]

    new_s.sort(key = len)

    for i in new_s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

# def solution(s):
#     answer = []
#     # 집합 길이 순으로 나열
#     # 앞에 원소 없는 것 찾아서 길이-1 인덱스에 넣기

#     s.sort(key = len) # 집합은 길이순으로 나열 못함 unhashable type: 'set' 
#     print(s)
#     # answer.append(s[0])
#     # print(answer)
#     # for i in range(1, len(s)):
#     #     answer.append(s[i]-s[i-1])


#     return answer