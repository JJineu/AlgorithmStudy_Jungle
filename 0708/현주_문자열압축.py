
def solution(s):
    answer = len(s)
    if len(s) <= 2:
        return len(s)

    for i in range(1, (len(s)//2) + 1):
        compressed = ""
        temp = s[:i]
        count = 1

        for j in range(i, len(s), i):
            if temp == s[j:j+i]: #이전 라운드때 설정한 temp, 현재의 s[j:j+i]
                count += 1
            else:
                if count != 1:
                    compressed += str(count)+temp
                else:
                    compressed += temp
                temp = s[j:j+i] #마지막 temp 설정, 이것까지 하고 for문 나갈 것임
                count = 1
        if count != 1:
            compressed += str(count)+temp
        else:
            compressed += temp
        
        answer = min(answer, len(compressed))
    
    # print(answer)
    return answer

solution("ababcdcdababcdcd")
