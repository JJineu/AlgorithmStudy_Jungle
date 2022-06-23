import sys
input = sys.stdin.readline

numA, numB = map(int, input().rstrip().split())
setA = set(map(int, input().rstrip().split()))
setB = set(map(int, input().rstrip().split()))

diffA = setA.difference(setB)
diffB = setB.difference(setA)
print(len(diffA) + len(diffB))