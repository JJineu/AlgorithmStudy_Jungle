from collections import deque

def solution(board, moves):
    answer = 0
    n = len(board)
    queue = [deque() for _ in range(n)]    
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                queue[j].appendleft(board[i][j])
    # for q in queue:
    #     print(q)

    stack = []
    for move in moves:
        move -= 1
        if queue[move]:
            stack.append(queue[move].pop())
            # print(stack)
            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
        else:
            continue
        
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) # 4