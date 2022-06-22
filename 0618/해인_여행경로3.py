from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    # {'ICN': ['BBB', 'AAA'], 'BBB': ['ICN']}

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]: # tmp를 기준으로 갈 곳 없으면
            answer.append(stack.pop())
            print('뭐지', answer)
        else: # tmp를 기준으로 갈 곳 있으면
            stack.append(routes[tmp].pop()) # tmp에서 갈 수 있는 곳 stack에 append
    answer.reverse()

    return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
#["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 1. "ICN" -> "AAA"
# 2. "ICN" -> "BBB"
# 3. "BBB" -> "ICN"
print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))
# "ICN" -> "BBB" -> "ICN" -> "AAA"