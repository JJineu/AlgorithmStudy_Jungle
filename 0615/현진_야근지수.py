# int not iterable 오류..- 해결// 입출력예시와 인자들어오는 위치가 다름

# 최대한 리스트 안에 있는 숫자가 비슷해야 한다
# 가장 큰 값 부터 - work, cnt+= 1 <= works
# works 만큼 뺄 수 있음
# 나머지 값 각각의 제곱의 합 리턴

from heapq import heappop, heappush

def solution(n, works):
    answer = 0
    h = []
    for i in works:
        heappush(h,-i)

    while h:
        n_work = heappop(h)*(-1)
        if n_work == 0:
            break
        heappush(h, -(n_work - 1))
        n -= 1
        if n == 0:
            break
            
    for i in h:
        answer += i*i

    return answer
    
solution([4, 3, 3],	4)
solution([2, 1, 2],	1)
solution([1,1],	3)