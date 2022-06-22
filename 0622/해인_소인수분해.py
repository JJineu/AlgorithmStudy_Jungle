import sys
input = sys.stdin.readline
n = int(input())
sosu = [False for _ in range(n)]

for i in range(2, n+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0: # 나눴을 때 한 번이라도 0이 된다면 소수 X
            break
    else:
        sosu[i-1] = True

# print(3//2) # 1 | 1, 2, 3
# print(6//2) # 3 | 1, 2, 3, 4, 5, 6
answer = []
def check(n):
    f = n//2
    s = f
    while f > 0 :
        if n % f == 0 and n % s == 0:
            if sosu[f] and sosu[s]:
                answer.append(sosu[f])
                answer.append(sosu[s])
            break
        else:
            f -= 1
            s += 1

for i in answer:
    print(i)

