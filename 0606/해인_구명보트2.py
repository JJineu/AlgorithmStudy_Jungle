def solution(people, limit):
    people.sort()
    i = 0
    j = len(people)-1
    answer = 0
    while i <= j:
        if people[i] + people[j] <= limit: # 맨 앞에 있는 애 + 맨 뒤에 있는 애 <= limit
            i += 1 # 맨 앞에 있는 애의 인덱스 하나 더하기 => 맨 앞 애 태운다는 뜻
        j -= 1     # 맨 뒤에 있는 애의 인덱스 하나 빼기   => 맨 뒤 애 태운다는 뜻
        answer += 1 # answer += 1
    return answer
        
    
    