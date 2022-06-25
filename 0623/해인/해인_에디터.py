# 최대 600,000글자까지 입력
# 커서
# 문장의 맨 앞 (첫번째 문자의 왼쪽)
# 문장의 맨 뒤 (마지막 문자의 오른쪽)
# 문장 중간 임의의 곳(모든 연속된 두 문자 사이)
import sys
input = sys.stdin.readline
from collections import deque

word = list(input().rstrip())
num = int(input())
left = deque(word)
right = deque()

while num >= 1:
    order = input().rstrip()
    if len(order) > 2:
        a, b = order.split()
    else:
        a = order
    if a == 'P': # P $ : $라는 문자를 커서 왼쪽에 추가함
        left.append(b)
    elif a == 'L': # L : 커서를 왼쪽으로 옮김
        if left:
            right.appendleft(left.pop())
    elif a == 'D': # D : 커서 오른쪽으로 옮김
        if right:
            left.append(right.popleft())
    else: # B : 커서 왼쪽에 있는 문자 삭제
        if left:
            left.pop()
    num -= 1

print("".join(left + right))

