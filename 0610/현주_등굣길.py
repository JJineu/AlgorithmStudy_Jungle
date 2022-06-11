# def solution(col, row, puddles):
    
#     # village = [[1 for _ in range(col+1)] for _ in range(row+1)]
#     dp_table = [[0 for _ in range(col+1)] for _ in range(row+1)]

#     def dfs(x, y):
#         if [x, y] not in puddles:
#             if x == row-1 and y == col:
#                 dp_table[x][y] = 1
#             elif x == row and y == col-1:
#                 dp_table[x][y] = 1
            
#             else:
#                 if x <= row-1:
#                     dp_table[x][y] += dfs(x+1, y)
#                 if y <= col-1:
#                     dp_table[x][y] += dfs(x, y+1)

#         return dp_table[x][y]

#     print(dfs(1,1))
#     answer = dfs(1,1)
#     return answer%1000000007

def solution(row, col, puddles):
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

    dp[1][1] = 1


    answer = dfs(1,1)
    return answer%1000000007

solution(4, 3, [[2,2]])