from sys import stdin 
input = stdin.readline 

def main():
    k, n = map(int, input().split())
    arr = []
    for _ in range(k):
        arr.append(int(input()))
    start = 1
    end = max(arr)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        cnt = 0
        for i in arr:
            cnt += i // mid
        # if cnt == n:
        #     print(mid)
        #     return
        if cnt >= n :
            start = mid +1
            ans = mid
        else: # cnt < n
            end = mid -1

    print(ans)
main()