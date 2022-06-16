def solution(n, computers):
    answer = 0
    parent = list(range(n+1))
    # print(parent)
    
    for i in range(n):
        for j in range(i,n):
            if computers[i][j] == 1:
                union(i+1,j+1,parent)
                # print(parent)                
    
    # find(2, parent)
    for i in range(1, n+1):
        find(i, parent)
        
    answer = len(set(parent)) - 1
    print(answer)
    return answer

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
        # print(parent)
    return parent[x]
    
def union(x,y, parent):
    a = find(x, parent)
    b = find(y, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return