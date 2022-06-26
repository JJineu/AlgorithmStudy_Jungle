# fffffffff
from sys import stdin 
input = stdin.readline
# from math import factorial
from itertools import permutations

def main():
    n = int(input())
    # num = factorial(n)

    s = [i for i in range(1,n+1)]
    # for i in range(n):
    #     tmp = s
    #     ans = []
    #     ans.append(i)
    #     while tmp:
    #         if a not in ans:
    #             ans.append(a)
            
    #     print(' '.join(ans))
    p_s = list(permutations(s,n))
    p_s.sort()
    for p in p_s:
        print(' '.join(list(map(str, p))))

main()

