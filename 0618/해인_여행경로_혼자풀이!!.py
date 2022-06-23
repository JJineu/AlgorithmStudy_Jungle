answer = []

def processing(tickets):
    adj_port = dict()
    
    for a, b in tickets:
        if a in adj_port:
            if b in adj_port[a]:
                adj_port[a][b] += 1
            else:
                adj_port[a][b] = 1
        else:
            adj_port[a] = {b:1}
    return adj_port

def btracking(adj_port, now_port, total_t, used_t = 0, path = ['ICN']):
    if used_t == total_t:
        answer.append(path.copy())
        return
    else:
        if now_port in adj_port:
            for next_port, cnt in adj_port[now_port].items():
                if cnt:
                    path.append(next_port)
                    adj_port[now_port][next_port] -= 1
                    btracking(adj_port, next_port, total_t, used_t+1, path)
                    adj_port[now_port][next_port] += 1
                    path.pop()

def solution(tickets):
    total_t = len(tickets)
    adj_port = processing(tickets)
    # adj_port {'ICN': {'SFO': 1, 'ATL': 1}, 'SFO': {'ATL': 1}, 'ATL': {'ICN': 1, 'SFO': 1}}
    btracking(adj_port, 'ICN', total_t)
    answer.sort() # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 
    return answer[0]
