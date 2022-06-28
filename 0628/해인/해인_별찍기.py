# 처음에 푼 풀이
# n = int(input())

# def drawStars(n):
#     stars = ['*']
#     if n == 1:
#         return stars
    
#     drawStars(n//3)
#     L = []

#     for star in stars:
#         L.append(star*3)
#     for star in stars:
#         L.append(star + (n//3)* " " + star)
#     for star in stars:
#         L.append(star*3)


# print("\n".join(drawStars(n)))

# 두번째로 푼 풀이
# n = int(input())

# def drawStars(n):
#     if n == 1:
#         return ['*']
    
#     stars = drawStars(n//3) # stars는 기존에 있던 L을 리턴받은 것
#     L = []

#     for star in stars:
#         L.append(star*3)
#     for star in stars:
#         L.append(star + (n//3)* " " + star)
#     for star in stars:
#         L.append(star*3)
    
#     return L

# print("\n".join(drawStars(n)))

# 세번째로 푼 풀이
n = int(input())

def makeStars(n):
    if n == 1:
        return ['*']
    stars = makeStars(n//3) # 이전 depth에서 돌았던 리턴값을 올라오면서 받음

    L = []
    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star + " "*(n//3) + star)
    for star in stars:
        L.append(star*3)

    return L

print("\n".join(makeStars(n)))