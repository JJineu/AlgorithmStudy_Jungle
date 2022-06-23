from sys import stdin 
input = stdin.readline

def main():
    a, b = map(int, input().split())
    li_a = list(map(int, input().split()))
    ans_a = len(li_a)
    li_b = list(map(int, input().split()))
    ans_b = len(li_b)
    for i in li_b:
        li_a.append(i)
    ans_c = len(set(li_a))
    ans = ans_a + ans_b - ans_c #교집합
    print(ans_c - ans)
    
main()

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