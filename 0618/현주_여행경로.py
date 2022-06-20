def solution(tickets):

    def dfs(ticket, v):

        route.append(v)

        if len(route)-1 == len(tickets):
            route_copy = route.copy()
            answer.append(route_copy)
            return

        for i in range(len(tickets)):
            if tickets[i][0] == v and used[i] == 0: #여기서 출발해서 갈 곳이 있다
                used[i] = 1
                dfs(i, tickets[i][1])
                route.pop()
                used[i] = 0
            
        return 

    answer = []
    # for t in range(len(tickets)):
    route = []
    used = [0] * len(tickets)
    dfs(0, tickets[0][0])

    #print(sorted(answer)[0])
    return sorted(answer)[0]


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])