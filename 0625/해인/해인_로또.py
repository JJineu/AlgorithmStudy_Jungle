# k개의 수를 골라 집합 S를 만듦
from itertools import combinations
while True:
    order = input()
    if order == '0':
        break
    else:
        num = list(order.split())
        n = num[0]
        num = num[1:]

        tmp = combinations(num, 6)

        for i in tmp:
            print(" ".join(map(str,i)))
    print() 
