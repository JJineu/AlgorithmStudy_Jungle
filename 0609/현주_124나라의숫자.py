from collections import deque

def get_ternary(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    # print(rev_base)
    print(rev_base[::-1])
    return rev_base[::-1]

def solution(n):
    # nums = [1, 2, 4]
    #0, 1, 2만 쓰는 3진법.

    if n < 4:
        if n == 1:
            print(1)
            return 1
        if n == 2:
            print(2)
            return 2
        else:
            print(4)
            return 4
    #자릿수가 넘어간다면
    stack = deque([get_ternary(n, 3)])
    # print(stack)
    answer = []
    while len(stack) > 0:
        x = stack.popleft()
        if x == '0':
            answer.append(1)
        elif x == '1':
            answer.append(2)
        else: #x == 2
            answer.append(4)
    print(*answer, sep = '')
    return answer
solution(6)
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
