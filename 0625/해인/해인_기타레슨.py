# 블루레이 개수 가급적 줄이기
# M개의 블루레이(같은 길이)에 모든 기타 강의 동영상 녹화
# 블루레이 크기(녹화 가능한 길이) 최소

# 각 강의의 길이 분 단위(자연수)
# 가능한 블루레이 크기 중 최소

n, m = map(int, input().split())
time = sorted(list(map(int, input().split())))

def bsearch(i):
    start = time[i]
    end = sum(time[-(n-m+(i+1)):])

    while start <= end:
        mid = (start + end)//2
        flag = False
        for t in time:
            if t > mid:
                flag = True
        if flag:
            return mid
        # else:
            

# print(mid)

for i in range(len(time)):
    bsearch(i)
