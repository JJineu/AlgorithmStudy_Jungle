import sys
input = sys.stdin.readline

target = input().rstrip()
explosion = input().rstrip()
stack = []

for i in range(len(target)):
    stack.append(target[i])
    if stack[-1] == explosion[-1]: # 탐색중인 글자와 폭팔문자의 젤 끝에 글자와 동일하다면
        # 지금까지 stack에 추가된 문자에서 폭팔문자 길이를 뺀곳에서부터 탐색해서 폭팔문자인지 확인하여서 제거한다.
        if ''.join(stack[len(stack)-len(explosion):]) == explosion:
            j = len(explosion)
            while j != 0:
                stack.pop()
                j -= 1
                if not stack:
                    break

if not stack:
    print('FRULA')
else:
    print(''.join(stack))