# 정수 x
n = input()
numdic = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

if len(n) == 1: # 십진수 확실
    print(int(n))
else:
    if n[:2] == '0x': # 16진수
        num = 0
        for i in range(2, len(n)):
            if n[i] in numdic:
                num += 16 ** (len(n)-i-1) * numdic[n[i]]
            else:
                num += 16 ** (len(n)-i-1) * int(n[i])
        print(num)
    else:
        if n[0] == '0': # 8진수
            num = 0
            for i in range(len(n)): # 0, 1, 2
                num += 8 ** (len(n)-i-1) * int(n[i])
            print(num)
        else: # 10진수
            print(int(n))
