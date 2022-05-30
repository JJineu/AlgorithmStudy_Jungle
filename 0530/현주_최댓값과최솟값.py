def solution(s):
    arr = list(map(int, s.split()))
    data = [str(min(arr)), str(max(arr))]
    answer = ' '.join(data)

    return answer

# solution("-1 -2 -3 -4")
# solution(s)