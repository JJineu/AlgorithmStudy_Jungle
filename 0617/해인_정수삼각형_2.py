import sys
input = sys.stdin.readline

n = int(input())
tri = [[] for _ in range(n)]

for i in range(n):
    tri[i] = [0] + list(map(int, input().split())) + [0]

print(tri)
