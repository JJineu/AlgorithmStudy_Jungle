import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    lec_lens = list(map(int, input().split()))
    if n == m:
        print(max(lec_lens))
        return

    left = sum(lec_lens) // m
    right = sum(lec_lens)

    ans = sys.maxsize
    while left <= right:
        mid = (left + right) // 2 # 길이 mid인 블루레이가 총 몇 개 필요한지 확인
        # print(f'mid: {mid}')
        cnt = 1
        tmp = 0
        flag = 1
        for i in range(n):
            if tmp + lec_lens[i] <= mid:
                tmp += lec_lens[i]
            else:
                cnt += 1
                if lec_lens[i] <= mid:
                    tmp = lec_lens[i]
                else:
                    flag = 0
                    break        

            # print(f'    cnt: {cnt}')
            if cnt > m:
                flag = 0
                break
        
        if flag:
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1            
    print(ans)

main()