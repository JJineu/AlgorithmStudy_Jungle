# 경업님 풀이 공부
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    lec_lens = list(map(int, input().split()))
    if n == m: # 강의의 수와 블루레이의 수가 같은 경우
        print(max(lec_lens)) # 최댓값이 크기가 됨
        return # 하나의 블루레이에 하나씩 강의를 담으면 되므로 return으로 바로 종료

    left = sum(lec_lens) // m # m개로 나눴을 때의 블루레이의 길이
    right = sum(lec_lens)     # 1개로 나눴을 때의 블루레이의 길이

    ans = sys.maxsize         # 강의 순서를 따로 정렬하고 푸는 게 아니므로 결과 대소도 제각각 
                              # => 큰 값 정해두고 min인 것을 결과로 추려내야
    while left <= right:
        mid = (left + right) // 2 # 길이 mid인 블루레이 -> 총 몇 개 필요한지 확인(아래 for문에서)
        # print(f'mid: {mid}')
        cnt = 1 # 블루레이 개수
        tmp = 0
        flag = 1  # 블루레이 개수가 m개보다 작으면
        for i in range(n):
            if tmp + lec_lens[i] <= mid: 
                # 블루레이 길이가 mid라면 최댓값이므로 (지금까지 값) + 현재값 <= mid 이면 
                # 블루레이 개수 그대로이고 tmp 값만 갱신
                tmp += lec_lens[i]
            else: # mid를 초과하면 새로운 블루레이에 넣어줌
                cnt += 1
                if lec_lens[i] <= mid:
                    tmp = lec_lens[i] # tmp를 새로 넣어준 값으로 초기화  

            if cnt > m: # 블루레이 개수가 m개보다 크면 for문에서 나감
                flag = 0
                break
        
        if flag: 
            # 블루레이 개수가 m개보다 작으면 블루레이 개수가 늘어나야 하므로
            # 블루레이 최대 길이가 줄어들어야 함 -> right = mid - 1
            ans = min(ans, mid)
            right = mid - 1
            print('flag가 true')
        else:
            # 블루레이 길이가 m개보다 크면 블루레이 개수가 적어져야 하므로
            # 블루레이 최대 길이가 늘어나야 해서 -> left = mid + 1
            left = mid + 1 
            print('flag가 false')           
    print(ans)

main()