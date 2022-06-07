import sys
input = sys.stdin.readline

#숫자를 적절히 더하고 빼서 target 만들기
#방법의 수 return
# 2 <= len(numbers) <=20



def solution(numbers, target):
#eval()
    cnt = 0
    ans = [0]
    for i in numbers:
        tmp = []
        for j in ans:
            tmp.append(j + i)
            tmp.append(j - i)
        ans = tmp
    
    for k in ans:
        if k == target:
            cnt += 1

    print(cnt)
    return cnt
        
    #     stackA.append('+' + str(i))
    #     stackB.append('-' + str(i))
    
    # temp = [None] * (len(numbers))
    # def dfs(temp, result, count = 0):
    #     if result == target and all(temp):
    #         count += 1
    #         return 
        
    #     for i in range(len(numbers)):
    #         if temp[i] == None:
    #             temp[i] = stackA[i]
    #             result = eval(str(temp))
    #             dfs(temp, result, count)
    #             temp[i] = stackB[i]
    #             result = eval(str(temp))
    #             dfs(temp, result, count)
        
    #     return count
    # print(dfs(temp, 0, 0))
    
solution([1, 1, 1, 1, 1], 3)