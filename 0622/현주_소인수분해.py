import sys
import math
input = sys.stdin.readline

def is_primary_number(n: int):
    if n>1:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
    return False

def main(N):
    
    if N == 1:
        return
    #nums = [i for i in range(1, N+1)]
    factors = []

    for x in range(2, int(math.sqrt(N)+1)):
        # print(x)
        if is_primary_number(x):
            while N % x == 0:
                factors.append(x)
                N //= x
                if N == 1:
                    [print(x) for x in factors]
                    return
    if N != 1:
        factors.append(N)     
    [print(x) for x in factors]
    return

N = int(input())
main(N)
# def factorization(x):
#     y = q.popleft()
#     while q:
#         if is_primary_number(y):
#             factors.append(y)
           