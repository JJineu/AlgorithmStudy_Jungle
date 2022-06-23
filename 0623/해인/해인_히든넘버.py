# 입력으로 주어진 단어에 숨어있는 모든 히든 넘버의 합
# 히든 넘버가 없는 경우에 0 출력
import sys
input = sys.stdin.readline

n = int(input())
word = input()
tmp = []
for w in word:
    if w.isdigit():
        tmp.append(w)
    else:
        tmp.append('!')

stack = ['0']
for t in tmp:
    if t.isdigit():
        if stack[-1].isdigit(): # 스택에 저장된 마지막 원소가 숫자일 때
            stack[-1] = stack[-1] + t # 마지막 숫자에 숫자문자열 더해주기
        else: # 스택에 저장된 마지막 원소가 !일 때
            stack.append(t) # 그냥 숫자만 append
    else:
        stack.append(t) # !일 땐 그냥 append

ans = 0
flag = False
for i in stack:
    if i != '!':
        ans += int(i)
        flag = True

if not flag:
    print(-1)
else:
    print(ans)