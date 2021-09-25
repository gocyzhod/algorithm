def solution(lottos, win_nums):
    answer = []
    
    # 1 ~ 45 6개 복권
    

    an = 0
    lotto0 = 0
    for number in lottos :
        if number == 0 :
            lotto0 += 1
            continue
        for win_num in win_nums :
            if number == win_num :
                an += 1
                
    while(True):
        if an <= 1 :
            answer.append(6)
        elif an == 2 :
            answer.append(5)
        elif an == 3 :
            answer.append(4)
        elif an == 4 :
            answer.append(3)
        elif an == 5 :
            answer.append(2)
        elif an == 6 :
            answer.append(1)
        if len(answer) == 2:
            break
        an += lotto0
    answer.sort()
    return answer
