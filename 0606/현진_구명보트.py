# 못품

def solution(people, limit):
    # q = deque()
    # for i in people:
        # q.append(i)

    people.sort(reverse = True)
    cnt = 1
    sum_w = 0

    while len(people) > 1:
        # print(len(people))
        # for i in range(len(people)):
        a = people.pop()
        # print(a)
        sum_w += a
        # print(sum_w)
        if sum_w > limit:
            cnt += 1
            people.append(a)
            break

    return cnt

solution([70, 50, 80, 50], 100)
