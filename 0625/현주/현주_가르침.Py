import sys
import string
input = sys.stdin.readline

#1<=N<=50
#0<=K<=26
'''-------------풀다가 포기함ㅋㅋㅋㅋㅋㅋ------------------'''
def main():
    N, K = map(int, input().split())
    alphabet = list(string.ascii_lowercase)
    words = []
    readable = [] #그때그때 활용할 버퍼
    bitmask = 1<<26
    count = 0
    visited = [0] * (N+1)
    literacy = []
    literate = 0

    #극단적인 케이스
    if K < 5: #a, n, t, c, i
        print(0)
        return
    if K == 26:
        print(N)
        return

    #get input
    for _ in range(N):
        words.append(list(input().rstrip()))

    def dfs(i):
        nonlocal bitmask, count, literate
        visited[i] = 1
        for letter in words[i]:
            bitmask = (bitmask | 1<<(alphabet.index(letter)))
        bitword = bitmask
        bitmask = 1<<26

        if countSetBits(bitword) <= K:
            readable.append(bitword)
            literate += 1

        # for i in range(len(readable)-1):
        if (readable[-1] | readable[-2]) > K:
            literate -= 1
            if all(visited):
                literacy.append(literate)
            return
        
        if all(visited):
            literacy.append(literate)
            return
        
        for j in range(N):
            if not visited[j]:
                dfs(j)
                visited[j] = 0
                readable.pop()

    for i in range(N):
        visited = [0]*(N+1)
        dfs(i)
    print(max(literacy))
    





def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

# def main():
#     N, K = map(int, input().split())
#     words = []
#     alphabet = list(string.ascii_lowercase)
#     for _ in range(N):
#         words.append(list(input().rstrip()))
#     readable = []
#     visited = [0]*(N+1)
 
#     for i in range(N):
#         bitmask = (1<<26)
#         visited[i] = 1
#         for j in words[i]:
#             bitmask = (bitmask | 1<<(alphabet.index(j)))
#             print(f'j = {j}, {bitmask}')
#         if countSetBits(bitmask) <= K:
#             readable.append(bitmask)
#             # print(countSetBits(bitmask))
        
#     print(readable)