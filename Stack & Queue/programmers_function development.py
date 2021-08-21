def solution(progresses, speeds):
    answer = []
    
    cnt = 0
    time = 0
    
    while len(progresses) > 0:

        
        
        if progresses[0] + speeds[0] * time >= 100 : # 100점이 넘는다면. 조건 충족
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            
            time += 1
    
    answer.append(cnt)
    
    return answer
