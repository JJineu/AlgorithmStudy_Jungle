# 갈색 = 가장자리
# 가로 * 2 + 세로 * 2 - 4 = 갈색
# 갈색 - 2가로 +4 = 2세로
# 세로 = 1/2(갈색 - 2가로 +4)

# 4 * 2 + 3 * 2 - 4 = 10

# 노란색
# (가로-1) * (세로-1) = 노란색
# (i-2 )* (0.5 * (brown - 2*i + 4) -2)

def solution(brown, yellow):
    ans = []

    for i in range(brown+1):
        if (i-2 )* (0.5 * (brown - 2*i + 4) -2) == yellow:
            ans.append(i)
    if len(ans) == 1:
        ans.append(ans[0])
    
    return ans[::-1]