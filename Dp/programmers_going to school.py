def solution(m, n, puddles):
    
    
    
   # for i in range(len(puddles)):
    #    puddles[i].reverse()
    
    dp = [[0] * (m+1) for i in range(n+1)]
    #print(dp)
    
    dp[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1 :
                continue
            if len(puddles) >= 1 and [j, i] in puddles :
                dp[i][j] = 0
            else :
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            
    answer = dp[n][m]
    
    return answer
