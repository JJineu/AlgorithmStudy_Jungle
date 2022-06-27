import sys
input = sys.stdin.readline

def main():
    N = int(input())
    hand = sorted(list(map(int, input().split())))
    M = int(input())
    compare = list(map(int, input().split()))
    answer = []

    def binSearch(c):
        Flag = False
        left = 0
        right = len(hand)-1

        while left <= right:
            mid = (left+right)//2
            m = hand[mid]

            if m > c:
                right = mid - 1
            elif m < c:
                left = mid + 1
            else:
                answer.append(1)
                Flag = True
                break
        if not Flag:
            answer.append(0)

    for c in compare:
        binSearch(c)

    print(' '.join(list(map(str, answer))))

main()