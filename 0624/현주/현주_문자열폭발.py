import sys
input = sys.stdin.readline

original = list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for i in original:
    stack.append(i)

    if len(stack) >= len(bomb):
        for i in range(1, len(bomb)+1):
            if stack[-i] != bomb[-i]:
                break
        else: #for문 다 통과했으면
            for _ in range(len(bomb)):
                stack.pop()
if stack:
    print(*stack, sep = '')
else:
    print('FRULA')
        
