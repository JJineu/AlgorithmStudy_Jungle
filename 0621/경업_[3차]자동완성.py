# N개의 단어, 2 <= N <= 100,000
# 최소 O(NlogN)으로 풀어야 한다

def solution(words:list):
    answer = 0
    words.sort()
    n = len(words)
    cnt_overlapped = [0 for _ in range(n)]

    def count(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1
            else:
                return cnt
        return cnt

    for i in range(n-1):
        cnt_overlapped[i] = count(words[i], words[i+1])

    for i in range(n):
        if i == 0: # 맨 앞
            if not cnt_overlapped[i]:
                answer += 1
            else:
                answer += cnt_overlapped[i]
        elif i == n-1:
            answer += cnt_overlapped[i-1] + 1
        else:
            answer += max(cnt_overlapped[i-1], cnt_overlapped[i]) + 1

    print(answer)
    return answer

solution(["go","gone","guild"])
solution(["abc","def","ghi","jklm"])
solution(["word","war","warrior","world"])
solution(["a","b","c","d","e"])