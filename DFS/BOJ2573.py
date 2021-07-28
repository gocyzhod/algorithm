import sys
import copy
input = sys.stdin.readline

sys.setrecursionlimit(100001)

a, b = map(int,input().split())


iceland = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
pointx = 0
pointy = 0

cnt = 0

arr= []

for i in range(a):
    tmp = list(map(int,input().split()))
    iceland.append(tmp)

arr = copy.deepcopy(iceland)

def dfs1(x,y,px,py):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < a and 0 <= ny < b :
            if iceland[nx][ny] == 0 :
                arr[px][py] -= 1


def dfs2(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < a and 0 <= ny < b :
            if iceland[nx][ny] != 0 and visited[nx][ny] == False :
                dfs2(nx,ny)







while(True):
    think = 0
    visited = [[False] * b for _ in range(a)]
    cnt += 1
    for i in range(a):
        for j in range(b):
            if arr[i][j] <= 0 and iceland[i][j] != 0 :
                iceland[i][j] = 0
                
    for i in range(a):
        for j in range(b):
            if iceland[i][j] != 0 :
            
                pointx = i
                pointy = j

                dfs1(i,j,pointx,pointy)

    for i in range(a):
        for j in range(b):
            if iceland[i][j] != 0 and visited[i][j] == False:
                dfs2(i,j)
                think += 1

    if think > 1:
        print(cnt-1)
        break
    elif think == 0 :
        print(0)






    
현재 출력초과 무한루프에 빠진것 같다. 약 70% 까지 통과하는데 그 이후에 통과하지 못하고 있다.
어디가 문제인지 확인해봐야함.
