from itertools import combinations

def solution(orders, course):
    answer = []
    L = []
    for i in range(len(orders)):
        L.append(len(orders[i]))

    arr = [[] for _ in range(max(L))]
    setarr = [[] for _ in range(max(L))]
    
    for i in range(len(arr)):
        for j in range(len(orders)):
            tmp = []
            tmp = list(combinations(orders[j],i+2))
            for x in range(len(tmp)):
                tmp[x] = list(tmp[x])
                tmp[x].sort()
                #tmp[x] = ''.join(list(tmp[x]))
            arr[i].extend(tmp)
    arr.sort()
    new = []
    #print(arr)
    
    for i in range(len(arr)):
        Max = 0
        
        for j in range(len(arr[i])):
            if arr[i].count(arr[i][j]) >= Max :
                Max = arr[i].count(arr[i][j])
                tmp = arr[i][j]
                if Max >= 2 :
                    if [tmp,Max] not in new :
                        new.append([tmp,Max])
    
    
    new.sort(key=lambda  x : (len(x[0]),x[1]),reverse=True)
    
    #print(new)
    #print()
    answer.append(''.join(list(new[0][0])))
    Max = new[0][1]
    for i in range(len(new)-1):
        #print(i, answer)
        if len(new[i][0]) != len(new[i+1][0]) :
            answer.append(''.join(list(new[i+1][0])))
            Max = new[i+1][1]
        elif len(new[i][0]) == len(new[i+1][0]) :
            if new[i+1][1] == Max :
                #print(new[i+1][0], new[i+1][1] ,new[i][0], new[i][1],i )
                answer.append(''.join(list(new[i+1][0])))
        
    answer.sort()
    #print(answer)
    
    
        
    return answer
