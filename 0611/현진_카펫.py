# 안됨
def solution(brown, yellow):
    answer = []

    s = brown + yellow
    for row in range(3, int(s**0.5)+1):
        col = int(s/row)

        a = col*2 + row*2 -2
        b = (col-2) * (row-2)
        
        if brown == a:
            # print(33333)
            if b == yellow:
                answer.append(col)
                answer.append(row)
            # print(answer)
            break
    return answer
    
solution(10,2)
solution(8,1)
solution(24,24)
