import sys
input = sys.stdin.readline

stack = list(input().rstrip())
M = int(input().rstrip())
temp = []

for _ in range(M):
    command = list(input().rstrip())
    # print(command)
    if command[0] == 'L':
        if stack:
            temp.append(stack.pop())
    elif command[0] == 'D':
        if temp:
            stack.append(temp.pop())
    elif command[0] == 'B':
        if stack:
            stack.pop()
    else: #P $
        stack.append(command[2])
    # print(f'stack = {stack}')
    # print(f'temp = {temp}')

for i in range(1, len(temp)+1):
    stack.append(temp[-i])
    
print(*stack, sep = '')











'''스택 안 쓴 버전'''
# cursor_idx = len(original)-1

# for _ in range(M):
#     command = list(input().rstrip())
#     # print(command)
#     if command[0] == 'L':
#         if cursor_idx >= 0:
#             cursor_idx -= 1
#     elif command[0] == 'D':
#         if cursor_idx < len(original)-1:
#             cursor_idx += 1
#     elif command[0] == 'B':
#         if cursor_idx >= 0:
#             del original[cursor_idx]
#             cursor_idx -= 1
#     else: #P $
#         original.insert(cursor_idx+1, command[2])
#         cursor_idx += 1
# print(*original, sep = '')


