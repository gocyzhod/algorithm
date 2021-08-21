def solution(brown, yellow):
    answer = []
    
    a = 0 
    b = 0
    
    yellow_l = []
    
    for i in range(1,yellow+1):
        if yellow % i == 0 :
            yellow_l.append([i,yellow//i])
    #print(yellow_l)
    
    for i in range(len(yellow_l)):
        if (yellow_l[i][0]+2) * 2 + (yellow_l[i][1]) * 2 == brown :
            if yellow_l[i][0] > yellow_l[i][1] + 2 :
                answer.append([yellow_l[i][0]+2, yellow_l[i][1]+2])
                break
            else :
                answer.append([yellow_l[i][1]+2, yellow_l[i][0]+2])
            
    #print(answer)
    
    
    return answer[0]




