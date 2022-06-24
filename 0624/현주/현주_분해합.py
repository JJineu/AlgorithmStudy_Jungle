import sys
input = sys.stdin.readline

def main():

    N = int(input())
    answer = 0
    start = N - 9*len(str(N))
    if start < 0: #ex. N = 12
        start = 1
    for i in range(start, N+1): #N=18일 때 N까지 봐야함
        nums = list(map(int, list(str(i))))
        # print(nums)
        if i + sum(nums) == N:
            answer = i
            break
    print(answer)

main()