from sys import stdin 
input = stdin.readline
from itertools import combinations

def main():

    while 1:
        s = list(map(int, input().split()))
        n = s[0]
        if n == 0:
            break
        s = s[1:]
        for c in combinations(s,6):
            print(' '.join(list(map(str, c))))
        print()
main()