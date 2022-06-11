import math

def solution(brown, yellow):
    total = brown + yellow
    divisors = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow%i == 0:
            row, col = yellow//i, i
            if 2*(row+2) + 2*(col+2) - 4 == brown:
                print([row+2, col+2])
                return [row+2, col+2]
    #         divisors.append((yellow//i, i))
    # for row, col in divisors:
    #     if (row+2)*2 + col*2 == brown and (row+2)*(col+2) == total:
    #         # print([row+2, col+2])
    #         return [row+2, col+2]

solution(10, 2)
solution(8,1)
solution(24,24)