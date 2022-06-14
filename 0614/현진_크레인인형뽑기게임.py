#스택에 같은 숫자 쌓이면 없어짐

def solution(board, moves):
    answer = 0
    stack = []
    n = len(board[0])
    
    for move in moves:
        for i in range(n):
            # print(board[i][move-1])
            if board[i][move-1] != 0:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    answer += 2
                else: 
                    stack.append(board[i][move-1]) 
                board[i][move-1] = 0
                # print(stack)
                break
    # print(stack)
    # k = len(stack)

    # while stack:
    #     # print(stack)
    #     a = stack.pop()
    #     cnt = 1
    #     while stack:
    #         if a != stack[-1]:
    #             if cnt>=2:
    #                 answer += cnt
    #             break
    #         # print(stack)
    #         stack.pop()
    #         # print(stack,'after')
    #         cnt += 1
            # print(cnt)

    # if stack and stack[-1] == board[i][move-1]:
    #     stack.pop()
    #     answer += 1
    # else:
    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	[1,5,3,5,1,2,1,4])