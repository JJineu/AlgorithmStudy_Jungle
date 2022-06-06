def solution(people, limit):
    # 테케만 맞음
    people.sort() # 오름차순으로 정렬
    stack = [people[0]]
    answer = 1
    for i in range(1, len(people)):
        if stack[-1] + people[i] <= limit:
            stack[-1] = stack[-1] + people[i]
        else:
            stack.pop()
            stack.append(people[i])
            answer += 1
    return answer
#     풀이 2. - 잘 안 풀림..
#     people.sort(reverse = True)
#     minus = []
#     for i in people:
#         minus.append(limit-i)
#     answer = 0
#     boat = [people[0]]
    
#     i = 0
#     while i < len(people):
#         if boat[-1] > minus[i]:
#             answer += 1
#         else:
#             boat.pop()
#             boat.append(minus[i])
#         i += 1
#     return answer
        

    
    