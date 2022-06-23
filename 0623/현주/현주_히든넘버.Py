import sys
input = sys.stdin.readline

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = int(input().rstrip())
word = list(input().rstrip())

making_num = []
answer = 0
for i in word:
    if i in nums:
        making_num.append(i)
    else:
        if len(making_num) > 0:
            number = int(''.join(making_num))
            answer += number
            making_num = []
        
print(answer)
