import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    # print(N, M)
    nums = list(map(int, input().split()))
    answer = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                result = nums[i] + nums[j] + nums[k]
                if result > M:
                    continue
                else:
                    if result > answer:
                        answer = result
    print(answer)
                    
main()


