from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

tmp = list(combinations(card, 3))
hubo = []
for i in tmp:
    if m - sum(i) >= 0:
        hubo.append(sum(i))

print(max(hubo))
    
