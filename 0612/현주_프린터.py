def solution(priorities, location):
    q = list(enumerate(priorities))
    cur = q[location]
    order = 0

    while q:
        doc = q.pop(0)
        for i in q:
            if i[1] > doc[1]:
                q.append(doc)
                break
        else:
            order += 1 #현재 priority가장 높아서 인쇄 성공
            if doc == cur:
                # print(order)
                return order
     

# solution([2, 1, 3, 2], 2)
solution([1,1,9,1,1,1], 0)