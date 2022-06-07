# 수 앞에 연산자 (+ or -)를 붙여서 계산
    # 두가지 경우만 고려
    # + - 두가지 연산 계속 누적 시킴
    # target과 같은 값 나오면 나온 수 만큼 cnt +
# 사용 가능한 수 numbers
# 만들려는 수 target
# 만들 수 있는 경우의 수 return

def solution(numbers, target):
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
    
    return cnt