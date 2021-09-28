def solution(s):
    ss = []
    for i in range(len(s)):
        ss.append(s[i])
    answer = []
    cnt = 0
    while(True):
        if len(ss) <= 0 :
            break
        elif ss[cnt] == 'z' :
            answer.append(0)
            for i in range(4):
                ss.pop(0)
        elif ss[cnt] == 'o':
            
            answer.append(1)
            for i in range(3):
                ss.pop(0)
                
        elif ss[cnt] == 't' :
            if ss[cnt+1] == 'w':
                answer.append(2)
                for i in range(3):
                    ss.pop(0)
            elif ss[cnt+1] == 'h':
                answer.append(3)
                for i in range(5):
                    ss.pop(0)
        elif ss[cnt] == 'f':
            if ss[cnt+1] == 'o':
                answer.append(4)
            elif ss[cnt+1] == 'i' :
                answer.append(5)
            for i in range(4):
                ss.pop(0)
                    
        elif ss[cnt] == 's':
            if ss[cnt+1] == 'i' :
                answer.append(6)
                for i in range(3):
                    ss.pop(0)
            elif ss[cnt+1] == 'e':
                answer.append(7)
                for i in range(5):
                    ss.pop(0)
        elif ss[cnt] == 'e':
            answer.append(8)
            for i in range(5):
                ss.pop(0)
        elif ss[cnt] == 'n':
            answer.append(9)
            for i in range(4):
                ss.pop(0)
        else :
            answer.append(ss.pop(0))

        
    #print(answer)
    return int(''.join(map(str, answer)))

"""
따로 함수로 빼내어 코드를 줄이고 싶었으나, 시간을 정해놓고 생각나는대로 바로바로 구현하여 코드가 길어졌다.
"""
