from sys import stdin 
input = stdin.readline

def main():
    n = input()
    if n[0] == '0':
        if n[1] == 'x': # 16진수
            li = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            answer = 0
            for i in range(2,len(n)-1):
                ans = li.index(n[i])
                # print(ans)
                answer += int(ans)*(16**(len(n)-2-i))
            print(answer)
            return

        else: # 8진수
            li = ['0','1','2','3','4','5','6','7']
            answer = 0
            for i in range(1,len(n)-1):
                ans = li.index(n[i])
                # print(ans)
                # print((len(n)-2-i))
                answer += int(ans)*(8**(len(n)-2-i))
                # print(answer)
            print(answer)
            return

    answer = int(n)
    print(answer)


main()