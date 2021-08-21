def solution(answers):
    answer = [0,0,0]
    onenum = [1,2,3,4,5]
    twonum = [2,1,2,3,2,4,2,5]
    thnum = [3,3,1,1,2,2,4,4,5,5]
    one = []
    two = []
    three = []
    L = len(answers)
    
    while(True):
        for i in onenum:
            one.append(i)
        if len(one) >= L :
            break
    
    while(True):
        for i in twonum:
            two.append(i)
        if len(two) >= L :
            break
            
    while(True):
        for i in thnum:
            three.append(i)
        if len(three) >= L :
            break
    
    for i in range(L):
        if answers[i] == one[i] :
            answer[0] += 1
        if answers[i] == two[i] :
            answer[1] += 1
        if answers[i] == three[i] :
            answer[2] += 1
    
    lastanswer = []
    
    
    for i in range(3):
        if max(answer) == answer[i] :
            lastanswer.append(i+1)
        
    
    return lastanswer








d
