# n = int(input())
# d = 2

# while d <= n:
#     if n % d != 0:
#         d += 1
#     else:
#         n //= d
#         print(d)

# 현진 언니 풀이 복습
def main():
    k = int(input())
    li = []

    for i in range(2, int(k**0.5) + 1): # int(n ** 0.5) + 1 : 제곱근 + 1까지 나눠서 다 나누지 않고 반만 나눔
        while 1:
            if k % i == 0: # 2로 되면 해당 수를 2로 끝까지 (나누어 떨어지지 않을 때까지) 나눔
                print(i)
                k //= i
            else: # 2를 3번 나눠서 9가 되었을 때 비로소 break하고 3으로 넘어감
                break
    if k != 1: # k가 1이 아니면 한 번 더 나눠져야 하므로 != 1이면 현재 k 출력
        print(k)

main()