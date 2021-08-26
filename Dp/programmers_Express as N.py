
def solution(N, number):
    answer = 2
    
    dp = [0] * 11
    dp[1] = [N]
    dp[2] = [N+N, N-N , 11*N , N//N, N*N]
    tmp = 4
    
    #print(dp)
    while (True) :

        if N == number :
            answer = 1
            break
        if number == N+N or number == N-N or number == N//N or number == 11*N or number == N-N :
            answer = 2
            break
            
        answer += 1
        tmp_arr = []
        if answer > 8 :
          #  print('error')
            answer = -1
            break
        
        
        for x in range(1,answer): # 1, 2
            for y in range(x,answer): # 1, 2 // 
                if x+y == answer :
                    #print(x, y)
            
                    for i in range(len(dp[x])):
                        for j in range(len(dp[y])):

                            tmp_arr.append(dp[x][i] + dp[y][j])
                            tmp_arr.append(dp[x][i] - dp[y][j])
                            tmp_arr.append(dp[y][j] - dp[x][i])
                            tmp_arr.append(dp[x][i] * dp[y][j])
                            if dp[x][i] != 0 :
                                tmp_arr.append(dp[y][j] // dp[x][i])
                            if dp[y][j] != 0 :
                                tmp_arr.append(dp[x][i] // dp[y][j])
            

        tmp_arrr = set(tmp_arr)
        tmp_arr = list(tmp_arrr)
            
        tmp_arr.append(int('1'*(answer))*N) # 예외처리

        #print(tmp_arr)
        if number in tmp_arr :
           # print('find')
          #  print(dp)
         #   print(answer)
            #print(tmp_arr)
            break
        else :
            
            dp[answer] = tmp_arr
            
            #print(dp)
            tmp+=1
        #print(answer)
        

    if answer == -1 :
        return answer
    #print(dp)
    return answer

  
  """
  --------------------------
  
  코드가 많이 더럽다.
  기본적인 발상은 이렇다.
  dp[1]  은 N 숫자 하나로만 표현가능한 것
  dp[2] 는 N 숫자 2개로만 표현가능한 것
  그렇다면 dp[3] 은? dp[1]과 dp[2] 의 사칙연산만 계산하면된다. 단, 예외적으로 NNN 같은 경우는 따로 넣어준다.
  ※단, 여기서 생각할 것이 하나가 더 있다.
  dp[5] 일 경우, dp[2] 사칙연산 dp[3] 도 가능하고 dp[1] 사칙연산 d[4] 도 가능하다. 이러한 경우들을 다 계산해주어야 한다.
  
  넓게 머릿속으로 생각할 수 있다면 충분히 풀 수 있을 것 같다. 
  나는 안 될것 같지만....ㅜㅠ
  
  """
