from sys import stdin 
input = stdin.readline

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    sangs = list(map(int, input().split()))
    
    cards.sort()
    s = [0]*len(sangs)
    
    for i in range(len(sangs)):
        start = 0
        end = len(cards)-1 # 범위를 정확히 해줄 것
        while start <= end:
            mid = (start+end)//2
            # print(sangs[i], cards[mid])
            if sangs[i] == cards[mid]:
                s[i] = 1
                break
            elif sangs[i] > cards[mid]:
                start = mid +1
            else:
                end = mid -1
    
    print(' '.join(list(map(str, s))))
main()



# import sys
# input = sys.stdin.readline

# # hash
# def main():
#     input()
#     cards = set(input().split())
#     print(cards)
#     input()
#     nums = input().split()
    
#     ans = []
#     for num in nums:
#         if num in cards:
#             ans.append('1')
#         else:
#             ans.append('0')
#     print(' '.join(ans))  

# main()