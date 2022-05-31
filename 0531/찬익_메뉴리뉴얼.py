from itertools import permutations
def solution(orders, course):
    # orders : 각 손님들이 주문한 단품 메뉴들이 문자열 형식으로 담긴 배열
    # course : 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열
    # 새로 추가하게될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return
    
    # 최소 2명의 손님에게서 주문된 구성만 후보
    
    arr = [0] * 100
    ans = []
    cor = []
    cnt = 0
    while cnt < len(course):
        m = 0
        for i in orders:
            for j in i:
                arr[ord(j)] += 1 
        for k in arr:
            m = max(k, m)

        loc = arr.index(m)
        ans.append(chr(loc))
        arr[loc] -= course[cnt]
        cnt += 1
        
        if max(arr) > 0:
            continue
        else:
            for i in course:
                cor = permutations(ans, course[i])
                print("".join(cor))
            exit(0)
            
    return  print(cor)   