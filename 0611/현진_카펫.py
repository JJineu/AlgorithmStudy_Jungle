def solution(brown, yellow):
    answer = []

    s = brown + yellow
    for row in range(3, int(s**0.5)+1):
        col = int(s/row)

        a = col*2 + row*2 -4
        b = (col-2) * (row-2)
        # print("a",a, brown)
        # print("b",b, yellow)
        if brown == a:
            if b == yellow:
                answer.append(col)
                answer.append(row)
                # if len(answer) == 2:
                break
            # print(answer)
            
    
    return answer
    
solution(10,2)
solution(8,1)
solution(24,24)
