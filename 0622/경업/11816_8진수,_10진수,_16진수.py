import sys
input = sys.stdin.readline


def to_normal(num: str, key: int):
    while num:
        print(num)
        num //= key

def main():
    num = input().strip()
    if num[0] == '0':
        if num[1] == 'x': # 16진수
            print(int(num, 16))
        else:
            print(int(num, 8))
    else:
        print(num)

main()