from heapq import heappush, heappop

def solution(n, works):
    answer = 0
    queue = []
    for work in works:
        heappush(queue, -work)

    while n:
        n -= 1

        tmp = heappop(queue)
        if tmp:
            tmp += 1
            heappush(queue, tmp)
        else:
            break

    for num in queue:
        answer += num**2

    # print(answer)
    return answer

solution(4, [4, 3, 3]) # 12
solution(1, [2, 1, 2]) # 6
solution(3, [1, 1]) # 0