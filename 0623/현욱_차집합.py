import sys
input = sys.stdin.readline

a, b = map(int,input().split())
list_A = list(map(str,input().split()))
list_B = list(map(str,input().split()))
list_R = list(set(list_A) ^ set(list_B))

print(len(list_R))


# 집합연산
# https://zetawiki.com/wiki/Python_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%ED%95%A9%EC%A7%91%ED%95%A9,_%EA%B5%90%EC%A7%91%ED%95%A9,_%EC%B0%A8%EC%A7%91%ED%95%A9,_%EB%8C%80%EC%B9%AD%EC%B0%A8
