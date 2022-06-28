from sys import stdin
input = stdin.readline 

def main():
    n = int(input()) # 배열의 크기
    k = int(input()) # 일차원 배열에서의 인덱스

    start = 0
    end = k
    while start <= end:
        mid = (start + end) //2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)
        
        if cnt >= k:
            end = mid-1
        else:
            start = mid +1
            
    print(start)
main()
