import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = []
count = int(input())

for i in range(count) :
    func = input().strip()
    if func[0] == 'P':
        stack1.append(func[2]) # 첫번째 스택에 추가
    elif func[0] == 'L' and stack1 != []:
        stack2.append(stack1.pop()) # 첫번째 스택에서 pop해서 두번째 스택으로 이동
    elif func[0] == 'D' and stack2 != []:
        stack1.append(stack2.pop()) # 두번째 스택에서 pop해서 첫번째 스택으로 이동
    elif func[0] == 'B' and stack1 != []:
        stack1.pop()

print("".join(stack1 + list(reversed(stack2))))


# 시간초과
# stack = list(input().rstrip())
# count = int(input())
# cursor = len(stack)

# for i in range(count) :
#     func = input().strip()
#     if func[0] == 'P':
#         stack.insert(cursor, func[2])
#         cursor += 1
#     elif func[0] == 'L':
#         if cursor != 0 :
#             cursor -= 1
#     elif func[0] == 'D':
#         if cursor != len(stack):
#             cursor += 1
#     elif func[0] == "B":
#         if cursor != 0 :
#             del stack[cursor - 1]
#             cursor -= 1

# print("".join(stack))

