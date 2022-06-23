# from sys import stdin 
# input = stdin.readline

# def p(n , li):
#     li = []
#     if n < 2:
#         return
#     if n >= 2:
#         li.append(2) 
#     for i in range(3, n+1):
#         for j in range(2, int(i**0.5) + 1):
#             if not li and i % j != 0:
#                 li.append(j)
#     return 

# def main():
#     k = int(input())
#     li = []
#     p(k, li)
#     for i in li:
#         while 1:
#             if k % i == 0:
#                 print(i)
#                 k //= i
#             else: return    


# main()

def main():
    k = int(input())
    li = []

    for i in range(2, int(k**0.5) + 1):
        while 1:
            if k % i == 0:
                print(i)
                k //= i
            else:
                break
    if k != 1:
        print(k)

main()