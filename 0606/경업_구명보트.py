def solution(people: list, limit: int):
    answer = 0
    people.sort()
    n = len(people)
    pl = 0
    pr = n-1
    while pl <= pr:
        answer+=1
        if n == 1:
            break

        if people[pl] + people[pr] <= limit:
            pl += 1
            pr -= 1
            n -= 2
            continue
        else:
            pr -= 1
            n -= 1

    print(answer)
    return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)