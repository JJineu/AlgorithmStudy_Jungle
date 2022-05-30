def solution(s):
    li = []
    for i in s:
        if i == " ":
            pass
        else:
            li.append(i)

    answer = []
    answer = min(li) + " " + max(li)

    return answer

# print(solution("1 2 3 4"))
