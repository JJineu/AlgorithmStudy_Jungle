# 1번 ~ n번
# 상대 순위가 바뀐 팀의 목록만 발표
# 올해 최종 순위?
# 확실한 올해 순위를 만들 수 없는 경우, 일관성이 없는 잘못된 정보
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input()) # 팀의 수 n
    old = list(map(int, input().split())) # 작년에 x등을 한 팀의 번호
    m = int(input()) # 상대적인 등수가 바뀐 쌍의 수 m
    new = [] # 상대적인 등수가 바뀐 두 팀
    for j in range(m):
        new.append(list(map(int, input().split())))

# n개의 정수를 한 줄에 출력
# 출력하는 숫자는 올해 순위
# 1등팀부터 순서대로 출력
# 확실한 순위를 찾을 수 없다면 ?
# 데이터에 일관성 없어서 순위 정할 수 없다면 "IMPOSSIBLE"