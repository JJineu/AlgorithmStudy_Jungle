def solution(s):
    d = {"zero": 0,
         "one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9}

    answer = []
    stack = []
    n = len(s)
    for i in range(n):
        if ord(s[i]) > 60:
            stack.append(str(s[i]))
            tmp = ''.join(stack)
            if tmp in d:
                answer.append(d[tmp])
                while stack:
                    stack.pop()
        else:
            if stack:
                tmp = ''.join(stack)
                answer.append(d[tmp])
                while stack:
                    stack.pop()
            answer.append(str(s[i]))

    print(int(''.join(list(map(str, answer)))))
    return int(''.join(list(map(str, answer))))


solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")