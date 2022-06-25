import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
target = list(map(str, input().strip()))
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= len(target):
        if stack[-len(target):] == target:
            for i in range(len(target)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
