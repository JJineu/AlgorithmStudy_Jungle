import sys
sys.setrecursionlimit(10**6)
def solution(tickets):
    tick = {}
    
    for i in range(len(tickets)):
        if tickets[i][0] not in tick:
            tick[tickets[i][0]] = [tickets[i][1]]
        else:
            tick[tickets[i][0]] += [tickets[i][1]]
    
    for i in tick:
        tick[i] = sorted(tick[i])

    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    # print(tick)
    answer = []
    def dfs(start):
        answer.append(start)
        if start in tick.keys():   
            flag = False
            for i in range(len(tick[start])): # 갈 수 있는 경로
                if tick[start][i][0] != '1': # 첫번째 단어가 1이 아니면 방문한 적 없는 것
                    tick[start][i] = '1' + tick[start][i]
                    dfs(tick[start][i][1:])
                    flag = True
        else:
            return
        
    dfs('ICN')
    
    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
#["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]