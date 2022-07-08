def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1): # s의 길이 1/2보다 크게 잘랐을 경우는 압축되지 않음
        compressed = "" # 압축된 문자열
        prev = s[0:step]
        cnt = 1
        
        for j in range(step, len(s), step): # step만큼 증가시키며 이전 문자열과 비교
            if prev == s[j:j+step]:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += str(cnt) + prev 
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1
        
        if cnt >= 2:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        
        answer = min(answer, len(compressed))
    
    return answer

# def solution(s):
#     answer = len(s)

#     # 1개 단위(step)부터 압축 단위를 늘려가며 확인
#     for step in range(1, len(s) // 2 + 1):
#         compressed = ""
#         prev = s[0:step]  # 앞에서부터 step만큼의 문자열 추출
#         count = 1
    
#     # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
#         for j in range(step, len(s), step):
        
#         # 이전 상태와 동일하다면 압축 횟수(count) 증가
#             if prev == s[j:j + step]:
#                 count += 1
            
#         # 다른 문자열이 나왔다면
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j + step]  # 다시 초기화
#                 count = 1
            
#         # 남아 있는 문자열에 대해서 처리
#         compressed += str(count) + prev if count >= 2 else prev
    
#         # 만들어지는 문자열이 가장 짧은 것이 정답
#         answer = min(answer, len(compressed))
