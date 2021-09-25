def solution(rows, columns, queries):
    answer = []
    
    puzzle = [[0] * columns for  _ in range(rows)]
    
    cnt = 1
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j] = cnt
            cnt += 1
        
    for i in range(len(queries)):
        for j in range(len(queries[i])):
            queries[i][j] -= 1
    
    cnt = 0
    while(True):
        if len(answer) == len(queries):
            break
        arr = []
        limitx = 0
        limity = 0
        x1 = queries[cnt][0]
        y1 = queries[cnt][1]
        x2 = queries[cnt][2]
        y2 = queries[cnt][3]
        #for i in puzzle :
         #   print(i)
        #print()
        
        if y2 == columns :
            limity = y2
        else :
            limity = y2 + 1
        
        for y in range(y1, limity):
            arr.append(puzzle[x1][y])
        for x in range(x1+1 , x2):
            arr.append(puzzle[x][y2])
        for y in range(limity,y1,-1):
            arr.append(puzzle[x2][y-1])
        for x in range(x2, x1+1,-1):
            arr.append(puzzle[x][y1])

        #print(arr)
        
        arr.insert(0,arr.pop())
        
        answer.append(min(arr))
        #print(answer)
        while arr :
            for y in range(y1, limity):
                puzzle[x1][y] = arr[0]
                arr.pop(0)
            for x in range(x1+1 , x2):
                puzzle[x][y2] = arr[0]
                arr.pop(0)
            for y in range(limity,y1,-1):
                puzzle[x2][y-1] = arr[0]
                arr.pop(0)
            for x in range(x2,x1+1,-1):
                puzzle[x][y1] = arr[0]
                arr.pop(0)

     #   for i in puzzle :
      #      print(i)
       # print()
            
            
        cnt += 1    
    
        
    #print(answer)
    return answer
