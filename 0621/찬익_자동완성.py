# 1. 완전탐색
# 시간초과 예상 
# 앞에서부터 문자 비교해오면서 달라지는 경우까지 카운트

# 2. 리스트 연산
# 리스트끼리 뺌 연산으로 중복 단어 제거
# 앞부분만 제거 가능할지?
# 뺀 값을 저장
'''
pseudo code
a = words[0][0]
result = words - a

b = words[0][1]
result2 = result - b
if len(result) == len(result2):
    break
...
    # words = words[::-1]
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            a = words[i]
            b = words[i][j]

            a_sub_b = [x for x in a if x not in b]
            print(a_sub_b)

'''

# 3. 스택 방식?
# 앞 부분부터 하나씩 날려보면서 비교해보는건 어떨까?
# 공통으로 제거되는게 있으면 추가로 돌려보는 방식

'''
  # print(words[0][0])
    cnt = 0
    startWord = words[0][0]
    stack = []
    for i in words:
        stack.append('')
        for j in i:
            stack.append(j)
    
    print(stack)
    
    while stack:
        for k in range(len(words)):
            if startWord == words[k][0]:
                cnt += 1
                # stack.pop([i][0])
                print(stack.pop([k][0]))

                # if words[0][1] == words[i][1]:

    print(stack)
            
    print(cnt)
    if cnt == 1:
        return len(words)
'''
def solution(words): 


    answer = 0
    return answer