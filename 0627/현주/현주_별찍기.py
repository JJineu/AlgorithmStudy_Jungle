import sys
input = sys.stdin.readline

N = int(input())

def makeStars(n):
    if n == 1:
        return ['*']
    stars = makeStars(n//3)

    L = []
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star + " "*(n//3) + star)
    for star in stars:
        L.append(star*3)
    
    return L

print("\n".join(makeStars(N)))