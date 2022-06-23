import sys
sys.setrecursionlimit(100000)
ans = []

def preprocessing(tickets):
    """adj_dict를 리턴"""
    adj_dict = {}
    for a, b in tickets:
        if a in adj_dict:            # 딕셔너리에 a가 존재하면
            if b in adj_dict[a]:     # 이미 a->b로 가는 티켓이 존재하면
                adj_dict[a][b] += 1  # 기존 티켓에 + 1
            else:                    # a->b로 가는 티켓이 존재하지 않으면
                adj_dict[a][b] = 1   # 티켓 = 1
        else:
             adj_dict[a] = {b : 1}   # 딕셔너리에 a가 존재하지 않으면
    
    return adj_dict
                 # 현재공항, 인접공항, 티켓 총 개수  , 사용된 티켓 개수, 지금까지 경로
def back_tracking(now_node, adj_dict, total_tickets, used_tickets=0, path = ['ICN']):
    if used_tickets == total_tickets:
        ans.append(path.copy())
    else:
        if now_node in adj_dict: # ABC의 경우 adj_dict에 키로 없음
            for adj_node, cnt in adj_dict[now_node].items():
                if cnt:
                    adj_dict[now_node][adj_node] -= 1
                    path.append(adj_node)
                    back_tracking(adj_node, adj_dict, total_tickets, used_tickets+1, path)
                    path.pop() # 여기서 pop됨
                    adj_dict[now_node][adj_node] += 1

def solution(tickets):
    total_tickets = len(tickets)
    adj_dict = preprocessing(tickets)
    print(adj_dict)
    # adj_dict {'ICN': {'SFO': 1, 'ATL': 1}, 'SFO': {'ATL': 1}, 'ATL': {'ICN': 1, 'SFO': 1}}
    back_tracking('ICN', adj_dict, total_tickets)
    ans.sort()
    
    return ans[0]
