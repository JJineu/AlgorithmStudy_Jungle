import sys
# t = int(input())

# num = [[] for _ in range(t)]

# for i in range(t):
#     num[i].append(map(int, input().split()))

# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if i == 1:
#         continue # continue는 for문 if문 같은 곳에서 사용 시, 다음 루프로 넘기는 역할을 함
        
#     for j in range(2, int(i**0.5)+1):  
#     # (2,int(i**0.5)+1, 2)로 하면 2,4 의 경우 2만 출력됨 (3을 건너뛰기 때문)
#         if i % j == 0:
#             break
#     else :
#         print(i)

i = 3

for j in range(2, int(i**0.5)+1):  
# (2,int(i**0.5)+1, 2)로 하면 2,4 의 경우 2만 출력됨 (3을 건너뛰기 때문)
    if i % j == 0:
        break
else :
    print(i)