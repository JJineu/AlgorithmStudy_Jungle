from collections import deque
n = int(input())
hide = input()

q = deque()
for i in hide:
    q.append(i)

numdict = dict()
for i in range(1, 10):
    numdict[str(i)] = 0
print(numdict)

tmp = []
while q:
    if q[0] not in numdict:
        q.popleft()
        tmp.append(-1)
    else:
        tmp.append(int(q.popleft()))

# for i in range(tmp):
#     if i != -1:
