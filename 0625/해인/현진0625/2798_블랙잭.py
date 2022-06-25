# from sys import stdin 
# input= stdin.readline
# from itertools import combinations


# def main():
#     n, m = map(int, input().split())
#     cards = list(map(int, input().split()))

#     s = []
#     max_s = 0
#     for i in combinations(cards, 3):
#         a = sum(i)
#         # print(a)
#         if a > m:
#             continue
#         max_s = max(max_s, a)
#     print(max_s)
        
# main()


# from sys import stdin 
# input= stdin.readline

# def main():
#     n, m = map(int, input().split())
#     cards = list(map(int, input().split()))
#     cards.sort()

#     ans = 0
#     for i in range(n-1,1,-1):
#         for j in range(i-1,0,-1):
#             for k in range(j-1,-1,-1):
#                 # print(i, j, k)
#                 # print(cards[i], cards[j], cards[k])
#                 tmp = cards[i] + cards[j] + cards[k]
#                 if tmp < ans:
#                     break
#                 if tmp <= m:
#                     ans = max(ans, tmp)
#     print(ans)

# main()



def recur(depth, start, sum):
    global ans
    if sum > m:
        return
    if depth == 3:
        # print(sum)
        ans = max(ans, sum)
        return
    for k in range(start, n):
        # print(depth, start, cards[k])
        recur(depth+1, k+1, sum + cards[k])

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
recur(0,0,0)
print(ans)
