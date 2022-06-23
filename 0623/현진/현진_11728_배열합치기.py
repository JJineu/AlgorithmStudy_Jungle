from sys import stdin 
input = stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)
    set(a)
    a.sort()
    # print(*a)
    print(' '.join(list(map(str, a))))
main()