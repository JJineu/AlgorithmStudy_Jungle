import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lect = list(map(int, input().split()))
def main():
    if n == m :
        print(max(lect))
        return
    
    start = sum(lect) // m  # 블루레이 길이의 최솟값
    end = sum(lect)         # 블루레이 길이의 최댓값
    ans = sys.maxsize

    while start <= end:
        mid = (start + end) // 2 # mid는 현재 블루레이 길이
        tmp = 0 # 현재 블루레이에 있는 길이
        cnt = 1 # 블루레이의 개수
        flag = 0 # mid 작아져야 하는 경우

        for i in range(len(lect)):
            if tmp + lect[i] <= mid: # 현재 블루레이에 담을 수 있을 때
                tmp += lect[i]
            else: # 현재 블루레이에 담을 수 없을 때
                if lect[i] <= mid: # 새로 담음
                    cnt += 1
                    tmp = lect[i]
                else: # 새로 담아도 mid보다 크기 클 때는 바로 break
                    flag = 1 # mid 커져야 하는 경우
                    break
        
        if cnt > m:
            flag = 1
        
        if flag: # mid 커져야 하는 경우
            start = mid + 1 
        else:
            ans = min(ans, mid)
            end = mid - 1
            
    print(ans)

main()

