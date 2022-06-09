# 4로 나눴을 때 몫과 나머지 
# 몫 0이면 나머지만
# 몫 1 이상이면 몫을 앞자리 

# 테스트 케이스만 통과
# -> 나머지는 내일 이어서

def solution(n):
    arr = [1,2,4]
    
    a = n // 4
    b = n % 4
    if a == 0:
        return str(arr[b-1])
    elif a != 0 and b:
        ans = 10*arr[a-1] + arr[b-1]
        return str(ans)
    elif a != 0 and not b:
        ans = 10*arr[a-1] + 1
        return str(ans)
    