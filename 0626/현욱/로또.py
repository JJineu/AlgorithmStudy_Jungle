import sys
input = sys.stdin.readline

while(True):
    a = list(map(int,input().split()))
    if a == [0]:
        break

    s,n = a[1:], a[0]-5

    def lotto(mini, r):
        if len(r) == 6:
            print(*r)
            return

        # 각 자리별로 숫자 조합 리스트 추출
        for i in s[len(r) : n+len(r)]:
            # 다음 자리의 숫자가 이전보다 작거나 같은 것이 나오면 안 된다.
            if i > mini :
                r.append(i)
                lotto(i,r)
                r.remove(i)

    lotto(0,[])
    print()