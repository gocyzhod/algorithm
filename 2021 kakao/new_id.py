def solution(new_id):
    answer = ''
    
    # 소문자
    idd = new_id.lower()
    # 규칙 제외 모두 삭제
    new = []
    for x in idd :
        if x.isdigit() == True or x.islower() == True or x == '-' or x =='_' or x =='.' :
            if x == '.' and len(new) >= 1:
                if new[-1] == '.' :
                    continue
            new.append(x)
    print(''.join(new))
    while(True):
        if len(new) > 0 and new[0] == '.' :
            new.pop(0)
        if len(new) > 0 and new[-1] == '.' :
            new.pop()
        if len(new) == 0 :
            break
        if new[0] != '.' and new[-1] != '.' :
            break
    print(''.join(new))
    if len(new) == 0 :
        new.append('a')
    if len(new) > 15 :
        while(True) :
            if len(new) <= 15 :
                break
            new.pop()
    if new[-1] == '.' :
        while(True):
            if len(new) > 0 and new[-1] == '.' :
                new.pop()
            if len(new) == 0 :
                break
            if new[0] != '.' and new[-1] != '.' :
                break
    elif len(new) <= 2 :
        while(True):
            if len(new) == 3 :
                break
            new.append(new[-1])
            
    answer = ''.join(new)
    
    return answer
