from collections import deque


def solution(number, k):
    
    """
    arr = list(combinations(number,len(number)-k))
    
    
    Max = 0
    
    for i in range(len(arr)):
        new = ''
        for j in range(len(arr[i])):
            new += arr[i][j]
        if Max <= int(new) :
            Max = int(new)
            answer = new
    """
    print(number)
    answer = ''
    arr = []
    num = []
    for i in number :
        num.append(int(i))
    num.reverse()
    
    for i in range(len(number)) :
        if k == 0 :
            break
        if len(arr) == 0 :
            arr.append(num.pop())
        else :
            if arr[-1] > num[-1] :
                arr.append(num.pop())
            else :
                for i in range(len(arr)):
                    if k == 0 :
                        break
                    if arr[-1] < num[-1] :
                        if len(arr) > 0 :
                            arr.pop()
                            k-=1
                        else :
                            break
                arr.append(num.pop())
   # print(num)
    if k == 0 and len(num) > 0 :
        for i in range(len(num)):
            arr.append(num.pop())
    for numm in arr :
        answer += str(numm)
    return answer
