from itertools import permutations

n = int(input())
num = []
for i in range(1, n+1):
    num.append(i)
tmp = list(permutations(num, n))

for i in tmp:
    print(" ".join(map(str, i)))