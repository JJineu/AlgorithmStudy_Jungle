import re
from collections import Counter

def solution(s:str):
    # s = Counter(re.findall('\d+', s))
    # print(s)
    
    s = s.replace("},","}.")
    ss = s[1:-1].split('.')
    # print(ss)

    ss.sort(key=len)
    for i in range(len(ss)):
        ss[i] = ss[i][1:-1]
        ss[i] = set(ss[i].split(','))
        
    # print(ss)

    ans = [int(list(ss[0])[0])]
    for i in range(1, len(ss)):
        ans.append(int(list(ss[i]-ss[i-1])[0]))

    print(ans)

solution("{{2},{21,12},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")