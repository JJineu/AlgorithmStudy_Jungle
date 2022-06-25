import sys
n = int(input())
card1 = sorted(list(map(int, input().split())))
m = int(input())
card2 = list(map(int, input().split()))

# for c in card2:
#     if c in card1:
#         print(1, end = " ")
#     else:
#         print(0, end = " ")

def bsearch(t) :
    start = 0
    end = len(card1)-1

    while start <= end:
        mid = (start + end)//2
        if card1[mid] == t:
            return True
        elif card1[mid] < t:
            start = mid + 1
        else:
            end = mid -1
    
    return False

for i in card2:
    if bsearch(i):
        print(1, end = " ")
    else:
        print(0, end = " ")        


