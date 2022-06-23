import sys
input = sys.stdin.readline

N = int(input())
alpha = str(input().rstrip())

text = ''
list_num = []
result = 0

for i in alpha :
  if i.isdigit() :
    list_num.append(str(i))
  else :
    if list_num :
      text = "".join(list_num)
      result += int(text)
      text = ''
      list_num = []

if list_num:
  text = "".join(list_num)
  result += int(text)

print(result)