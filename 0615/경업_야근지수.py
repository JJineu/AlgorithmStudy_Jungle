from heapq import heappush, heappop

def solution(n, works):
    answer = 0
    queue = []
    for work in works:
        heappush(queue, -work)

    while n:
        n -= 1
        if not queue:
            break

        tmp = heappop(queue)
        if tmp:
            tmp += 1
            heappush(queue, tmp)
        else:
            heappush(queue, 0)

    for num in queue:
        answer += num**2

    return answer

solution([4, 3, 3], 4) # 12
solution([2, 1, 2], 1) # 6
solution([1, 1], 3) # 0