# 인형이 없는 곳에서 크레인 작동시키면 아무 일도 일어나지 않음
# 크레인 모두 작동시킨 후 터트려져 사라진 인형의 개수 return
# 0은 빈칸
# 같은 숫자는 같은 모양의 인형
def solution(board, moves):
    boardL = [[] for _ in range(len(board[0]))]
    board = board[::-1]
    # board
    # [[3, 5, 1, 3, 1], [4, 2, 4, 4, 2], [0, 2, 5, 0, 1], [0, 0, 1, 0, 3], [0, 0, 0, 0, 0]]
    
    for i in range(len(board[0])): # 0, 1, 2, 3, 4
        for j in range(len(board[i])):
            if board[j][i] != 0:
                boardL[i].append(board[j][i])
    # boardL [[3, 4], [5, 2, 2], [1, 4, 5, 1], [3, 4], [1, 2, 1, 3]]
    bucket = []
    cnt = 0
    for i in moves:
        if len(boardL[i-1]) > 0:
            a = boardL[i-1].pop() # 보드에서 빼냄
            if len(bucket) > 0:
                if bucket[-1] == a:
                    bucket.pop()
                    cnt += 2
                else:
                    bucket.append(a)
            else:
                bucket.append(a)
            
    return cnt
