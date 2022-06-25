import sys
input = sys.stdin.readline

def main():
    n = int(input())
    word = input().strip()
    
    stack = []
    i = 0
    ans = 0
    while n > 0:
        if ord(word[i]) < 58:
            stack.append(word[i])
        else:
            if stack:
                if stack[0] == '0':
                    stack.pop(0)
                ans += int(''.join(stack))   
                stack = []
        
        i += 1
        n -= 1
    
    if stack:
        if stack[0] == '0':
            stack.pop(0)
        ans += int(''.join(stack))
    print(ans)
main()