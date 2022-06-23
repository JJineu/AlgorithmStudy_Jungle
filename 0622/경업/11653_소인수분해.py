import sys
input = sys.stdin.readline

def main():
    n = int(input())
    key = 2
    ans = []

    while n > 1:
        # print(n)
        if n % key == 0:
            ans.append(str(key))
            n //= key
        else:
            key += 1

    print('\n'.join(ans))        

main()