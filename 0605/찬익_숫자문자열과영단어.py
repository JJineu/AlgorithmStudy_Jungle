def solution(s):
    stack = []
    answer = []
    for i in s:
        stack.append(i)
        
    while stack:
        j = stack.pop(0)
        if(ord(j) >= 48 and ord(j) <= 57):
            answer.append(j)
        else:
            if j == 'z':
                # while not (ord(j))>= 48 and notord(j) <= 57 :
                #     stack.pop(0)    
                stack.pop(0)
                stack.pop(0)
                stack.pop(0)
                answer.append('0')
            if j == 'o':
                # while not (ord(j))>= 48 and notord(j) <= 57 :
                #     stack.pop(0)    
                stack.pop(0)
                stack.pop(0)
                answer.append('1')
            if j == 't':
                if stack.pop(0) == 'w':
                    stack.pop(0)
                    answer.append('2')
                else :
                    # while not (ord(j))>= 48 and notord(j) <= 57 :
                    #     stack.pop(0)    
                    stack.pop(0)
                    stack.pop(0)
                    stack.pop(0)
                    answer.append('3')
            if j == 'f':
                if stack.pop(0) == 'o':
                    # while not (ord(j))>= 48 and notord(j) <= 57 :
                    #     stack.pop(0) 
                    stack.pop(0)
                    stack.pop(0)
                    answer.append('4')
                else:
                    # while not (ord(j))>= 48 and notord(j) <= 57 :
                    #     stack.pop(0) 
                    stack.pop(0)
                    stack.pop(0)
                    answer.append('5')
            if j == 's':
                if stack.pop(0) == 'i':
                    stack.pop(0)
                    answer.append('6')
                else:
                    # while not (ord(j))>= 48 and notord(j) <= 57 :
                    #     stack.pop(0)    
                    stack.pop(0)
                    stack.pop(0)
                    stack.pop(0)
                    answer.append('7')
            if j == 'e':
                # while not (ord(j))>= 48 and notord(j) <= 57 :
                #     stack.pop(0)  
                stack.pop(0)
                stack.pop(0)
                stack.pop(0)
                stack.pop(0)
                answer.append('8')
            if j == 'n':
                stack.pop(0)  
                stack.pop(0)
                stack.pop(0)
                answer.append('9')
    answer = ''.join(answer)
    return int(answer)
