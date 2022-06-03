def solution(places):
    answer = []
    # 같은 행 확인
    flag = False
    for i in range(5): # 하나의 대기실
        for k in range(5): # 대기실에서 한 줄
            for j in range(3): # 한 줄마다 요소
                if places[i][k][j] == "P" and places[i][k][j+1] == "P":
                    flag = True
                    break
                elif places[i][k][j] == "P" and places[i][k][j+2] == "P" and places[i][k][j+1] == "O":
                    flag = True
                    break
            if places[i][k][3] == "P" and places[i][k][4] == "P":
                flag = True
        if not flag:
            answer.append(1)
        else:
            answer.append(0)
        flag = False
        
    # 위 아래 확인
            
    return answer