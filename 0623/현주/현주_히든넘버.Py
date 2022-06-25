import sys
input = sys.stdin.readline

# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = int(input().rstrip())
word = list(input().rstrip())

making_num = []
answer = 0
for i in word:
    if i.isdigit():
        making_num.append(i)
        if len(making_num) >= 6:
            number = int(''.join(making_num))
            answer += number
            making_num = []
    else:
        if len(making_num) > 0:
            number = int(''.join(making_num))
            answer += number
            making_num = []
#숫자로 끝날 경우
if making_num:
    number = int(''.join(making_num))
    answer += number
        
        
print(answer)
