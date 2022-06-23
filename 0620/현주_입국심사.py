'''right = 1e6 이런걸로 하면
    테케 7, 8 런타임에러'''

def solution(n, times):
    left = 0
    right = max(times)*n #포인트!!

    while left <= right:
        mid = (left+right)//2
        done = 0

        for t in times:
            done += mid//t
            if done >= n:
                answer = mid
                right = mid - 1
                break
     
        # if done >= n:
        #     answer = mid
        #     right = mid-1
        else: #done < n
            left = mid + 1
    # print(int(answer))
    return int(answer)

solution(6, [7, 10])