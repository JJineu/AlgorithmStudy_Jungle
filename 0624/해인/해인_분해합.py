import sys
input = sys.stdin.readline

num = int(input())
arr = [str(i) for i in range(1, num + 1)]
start = 0
end = int(arr[-1])

flag = False
for i in arr:
    tmp = int(i)
    for j in i:
        tmp += int(j)
    if tmp == num:
        print(i)
        flag = True
        break

if not flag:
    print(0)

# while start <= end :
#     mid = (start + end) // 2

#     tmp = int(arr[mid])
#     for j in arr[mid]:
#         tmp += int(j)
    
#     if tmp < num:
#         start = mid + 1
#         print(arr[mid])
#     elif tmp > num:
#         end = mid - 1
#         print(arr[mid])
#     else:
#         print(arr[mid])
#         print('헬로')
#         break


