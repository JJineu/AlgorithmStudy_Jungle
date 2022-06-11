# 중앙에는 노란색
# 테두리 1줄은 갈색
# 카펫의 가로, 세로 크기를 배열에 담아 리턴
def solution(br, ye):
    x = 1 # 가로
    y = 1 # 세로
    yak = []
    
    for i in range(1, ye + 1):
        if ye % i == 0:
            yak.append(i)
    if len(yak) == 1:
        yak.append(1)
        
    print(yak) 
    answer = []    
    for i in range(len(yak)):
        if (yak[i]+2) * (yak[len(yak)-i-1]+2) == br + ye:
            answer.append(yak[i]+2)
            answer.append(yak[len(yak)-i-1] + 2)
            break
        
    answer = sorted(answer, reverse = True)
    return answer
