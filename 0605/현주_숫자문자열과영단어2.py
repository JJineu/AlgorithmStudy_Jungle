import sys
input = sys.stdin.readline
numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven": 7, "eight": 8, "nine": 9}


def solution(slist):
    stack = []
    answer = []

    for i in slist:
        if i in list(map(str, numbers.values())):
            answer.append(int(i))
        else: # if string
            stack.append(i)
            if len(stack) >= 3: #제일 짧은 숫자가 one, two
                temp = ''.join(stack)
                if temp in numbers: #이렇게 하면 키값 중에 있는지 비교해줌
                    answer.append(numbers[temp])
                    stack = [] #clear과 이것중에 뭐가 더 효율적일까
            
    return int(''.join(list(map(str,answer))))
    # print(*answer, sep = '')
    


solution("one4")
solution("2three45sixseven")