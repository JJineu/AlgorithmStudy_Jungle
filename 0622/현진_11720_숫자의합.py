from sys import stdin 
input = stdin.readline

def main():
    n = int(input())
    s = str(input())
    sum = 0
    for i in range(n):
        a = s[i]
        sum += int(a)
    print(sum)
main()