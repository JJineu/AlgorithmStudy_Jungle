import math
import math

def solution(n, k):
    k -= 1
    answer = []
    numbers = list(range(1, n+1))
    
    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i-1))
        answer.append(numbers.pop(div))
        
    return answer



# def solution(n, k):
#     answer = [i for i in range(1, n+1)]
#     stack = []
#     k -= 1 #우리는 인덱스 찾는 거니까

#     while answer:
#         a = k//math.factorial(n-1) #n의 자리가 바뀔 때마다 (n-1)! 가지 가능성 
#         stack.append(answer[a])
#         del answer[a]

#         k = k % math.factorial(n-1)
#         n -= 1

#     return stack

# def solution(n, k):
#     people = [i for i in range(1, n+1)]
#     visited = [0 for _ in range(n)]
#     count = 0
#     perm = []

#     def dfs(perm, count=0):
#         if len(perm) == n:
#             count += 1
#             # if count == k:
#             #     return perm
#             return
        
#         for i in range(n):
#             if not visited[i]:
#                 visited[i] = 1
#                 perm.append(people[i])
#                 # print(perm)
#                 dfs(perm, count)

#                 if count == k:
#                     print(perm)
#                     return perm
#                 else:
#                     visited[i] = 0
#                     perm.pop()
#         return

    
#     dfs(perm, count)

#     print(perm)

solution(3, 5)

