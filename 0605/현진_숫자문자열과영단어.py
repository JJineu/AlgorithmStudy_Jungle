def solution(s:str):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = 0

    for i in range(10):
        s = s.replace(number[i], str(i))
    answer = int(s)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
