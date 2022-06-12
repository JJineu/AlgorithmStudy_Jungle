def solution(priorities:list, location):
    n = len(priorities)
    for i in range(n):
        priorities[i] = (i, priorities[i])

    target = priorities[location]
    
    cnt = 1
    while priorities:
        idx, val = priorities.pop(0)

        if not priorities:
            print(cnt)
            return cnt

        tmp = list(v for i, v in priorities)        
        if val < max(tmp):
            priorities.append((idx, val))
        else:
            if (idx, val) == target:
                print(cnt)
                return cnt
            cnt += 1

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)