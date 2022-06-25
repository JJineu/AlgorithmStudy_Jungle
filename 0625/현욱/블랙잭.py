import sys
input = sys.stdin.readline

N, M = list(map(int, input().split())) # 5 21
card_list = list(map(int, input().split()))

result = 0

for i in range(N-2) :
    for j in range (i+1, N-1) :
        for k in range (j+1, N) :
            temp = card_list[i]+card_list[j]+card_list[k]
            if temp < result :
                break

            if temp <= M :
                result = max(result, temp)

print(result)