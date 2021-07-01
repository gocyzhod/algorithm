import sys
input = sys.stdin.readline


n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]


w=0
b=0


def cal(x,y,n):         # cal(x위치,y위치,길이)
    global b,w
    now = arr[x][y]             # check = arr[0][0]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if now!=arr[i][j]:            #처음 칸과 일치하지 않는다면 
                                                #  4등분함
                cal(x,y,n//2)   #1
                cal(x,y+n//2,n//2)#2
                cal(x+n//2,y,n//2)#3
                cal(x+n//2,y+n//2,n//2)#4
                
                return 0  # 왜 써야하는진 모르겠음.

    if now==0:
        w+=1
        return 0
    else:   
        b+=1
        return 0
cal(0,0,n)
print(w)
print(b,end = '')
