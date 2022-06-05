import sys
input = sys.stdin.readline
numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


def solution(slist):
    keylist = list(map(str, numbers.keys()))
    letters = []
    answer = []

    for i in slist:
        if i in keylist:
            answer.append(int(i))
        else: # if string
            if len(letters) > 0:
                letters.append(i)
                n_string = ''.join(letters)
                if n_string in numbers.values():
                    answer.append(*[k for k, v in numbers.items() if v == n_string])
                    letters.clear()
            else:
                letters.append(i)
    return int(''.join(list(map(str,answer))))
    # print(*answer, sep = '')
    


solution("one4")
solution("2three45sixseven")