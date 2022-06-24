import sys
input = sys.stdin.readline

target = int(input())
num = len(str(target))
start = target - (num * 9) # 각 자리수의 최대는 9이기 때문에 자릿수*9뺀 곳에서 시작점을 정한다.
if start < 0 : # 뺐을 경우 음수 일 경우 양수에서 시작
    start = 0

for i in range(start, target+1) : # 입력값인 분해합만큼 돌릴 경우는 없지만 예외 케이스에 대비해서 끝까지 돌린다.
    nums = list(map(int, str(i)))
    result = sum(nums) + i # 분해합에 필요한 요소들을 다 더한다
    if result == target : # 분해합이 맞으면 생성자를 출력
        print(i)
        break
    if i == target : # 없을 경우는 0을 출력
        print(0)

# 진짜로 브루트포스로 탐색하려고 while문 사용, 시간초과
# target = int(input()) # 216
# temp = 0
# result = 0
# while target != temp :
#     temp = 0
#     result += 1
#     temp += result
#     for i in str(result) :
#         temp += int(i)

# print(result)
