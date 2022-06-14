def solution(board, moves):
    toys = [[] for _ in range(len(board[0]))]
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            toys[i].append(board[j][i])
    # print(toys)

    stack = []
    count = 0
    for i in moves:
        if toys[i-1]: #그 column에서 pop
            x = toys[i-1].pop(0)
            while x == 0 and toys[i-1]:
                x = toys[i-1].pop(0)
           
            if x == 0:
                continue
            if stack and stack[-1] == x:
                stack.pop()
                count += 2
                continue
            stack.append(x)

    return count

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])