import sys
input = sys.stdin.readline

def main():
    # 입력부
    n,s = map(int, input().split())
    a = list(map(int, input().split()))

    # 이분 분할
    m = n//2
    n = n - m

    # 왼쪽 부분집합의 모든 조합의 합을 저장할 list
    first = [0] * (1<<n)

    # 비트마스킹을 이용하여 Subset의 합을 담는다
    for i in range(1<<n): # 모든 부분수열 탐색 (00001, 00010, 00011, 00100, 00101, 00110, 00111, 01000, ...)
        for k in range(n): # 해당 부분수열에 k번째 수가 포함되니? 확인
            if (i&(1<<k)) > 0:
                # print(f"i&(1<<k): {i&(1<<k)}, i: {i}, k: {k}")
                first[i] += a[k]
                # print(f'first: {first}')
                
    # 오른쪽 부분집합의 모든 조합의 합을 저장할 list
    second = [0]*(1<<m)
    for i in range(1<<m):
        for k in range(m):
            if (i&(1<<k)) > 0:
                second[i] += a[k+n]
                # print(f'second: {second}, i: {i}, k: {k}')
                
    # first 오름차순 정렬, second 내림차순 정렬
    first.sort() # 좌측 절반,
    second.sort(reverse = True) # 우측 절반 부분수열의 모든 합이 저장되어 있음. 그것을 정렬

    n = 1<<n
    m = 1<<m
    pf = 0
    ps = 0

    ans = 0
    if s == 0:
        ans -= 1

    while pf < n and ps < m:
        val = first[pf] + second[ps]
        
        if val == s:
            pf += 1
            ps += 1
            
            cntf = 1
            while pf < n and first[pf] == first[pf - 1]:
                pf += 1
                cntf += 1    
            cnts = 1
            while ps < m and second[ps] == second[ps - 1]:
                ps += 1
                cnts += 1

            ans += cntf * cnts
        elif val < s:
            pf += 1
        else:
            ps += 1

    print(ans)
main()