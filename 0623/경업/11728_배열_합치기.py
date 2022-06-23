import sys
input = sys.stdin.readline

def main():
    # 각 배열의 크기가 최대 1,000,000
    # 그냥 합치면 N == 2,000,000
    # 시간제한 1.5초
    # O(NlogN)은 약 2,000,000 * 21 == 42,000,000 < 1초
    input()
    a = list(map(int, input().split()))
    b = a + list(map(int, input().split()))
    b.sort()
    print(' '.join(list(map(str, b))))

main()