import sys
input = sys.stdin.readline

N = str(input().rstrip())
if N[0] == '0':
    if N[1] == 'x':
        answer = int(N, 16)
    else:
        answer = int(N, 8)
else:
    answer = int(N)
print(answer)


# X = list(input().rstrip())

# if X[0] == '0':
#     if X[1] == 'x': #16진수
#         answer = 0
#         for i in range(1, len(X)-1):
#             j = X[-i]
#             if j == 'a':
#                 num = 10
#             elif j == 'b':
#                 num = 11
#             elif j == 'c':
#                 num = 12
#             elif j == 'd':
#                 num = 13
#             elif j == 'e':
#                 num = 14
#             elif j == 'f':
#                 num = 15
#             else:
#                 num = int(j)
#             answer += num * (16**(i-1))
#         print(answer)
            

#     else: #8진수
#         answer = 0
#         for i in range(1, len(X)):
#             answer += X[-i] * (8**(i-1))
#         print(answer)
    
# else:
#     answer = ''.join(X)
#     print(int(answer))

        