def solution(tickets):

    def dfs(t, v):
        # used[t] = 1
        route.append(v)
        # print(f'used = {used}')
        # print(f'route = {route}')

        if len(route)-1 == len(tickets):
            answer.append(route)
            print(f'answer = {answer}')
            return

        for i in range(len(tickets)):
            # print(f'i = {i}')
            # print(tickets[i][0])
            # print(used)
            if tickets[i][0] == v and used[i] == 0:
                used[t] = 1
                dfs(i, tickets[i][1])
                route.pop()
                used[t] = 0
                # print(f'answer pop됐니...? {answer}')
                
        return 

    answer = []
    for t in range(len(tickets)):
        print(f'dfs({t, tickets[t][0]}) 들어감')
        route = []
        used = [0] * len(tickets)
        dfs(t, tickets[t][0])

    print(answer)

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])