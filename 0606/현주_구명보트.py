'''시간초과'''
import sys
input = sys.stdin.readline

def solution(people, limit):
    count = 0
    ppl = sorted(people) #오름차순!!
    i = 0
    j = len(ppl)-1

    while i <= j:
        if ppl[i] + ppl[j] <= limit:
            i += 1
        j -= 1
        count += 1
    # print(count)
    return count
    
   



solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)




    # for i in range(l):
    #     if not visited[i]:
    #         count += 1  #배 하나 꺼내서
    #         visited[i] = 1 #앞에서 한 명 태움
    #         boat = [ppl[i]] 

    #         for j in range(1, l+1):
    #             if visited[-j]: #더 큰 애 알아봐
    #                 continue
    #             if sum(boat) + ppl[-j] <= limit:
    #                 visited[-j] = 1
    #                 boat.append(ppl[-j])
    #             else: #if i + ppl[-j] > limit:
    #                 boat.clear() #이번 배는 여기서 끝
    #                 break
    #     else: break

    # # print(count)
    # return count
