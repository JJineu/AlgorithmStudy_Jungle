word = list(input().strip())
bomb = list(input().strip())
stack = []

for i in range(len(word)):
    stack.append(word[i])
    if word[i] == bomb[-1]:
        if len(stack) >= len(bomb):
            if stack[-len(bomb):] == bomb:
                for i in range(len(bomb)):
                    stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")