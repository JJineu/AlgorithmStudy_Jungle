def solution(numbers, target):
    cnt = 0
    ans = [0]
    
    for i in numbers: # [4, 1, 2, 1]
        tmp = []
        for j in ans:
            tmp.append(j + i)
            tmp.append(j - i)
        ans = tmp # tmp에 append된 결과를 ans에 넣어줌
        print(ans)
    for k in ans:
        if k == target:
            cnt += 1
    
    return cnt

print(solution([4, 1, 2, 1], 4))