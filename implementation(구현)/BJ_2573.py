import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


## 15 : 45

r ,c = map(int,input().split())

answer = 0  # 최종답

arr = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(r):
    tmp = list(map(int,input().split()))

    arr.append(tmp)





def dfs2(x,y):
    
    visited[x][y] = 7
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 4 :

            if arr[nx][ny] == 0 :   # 빈 공간이라면
                dfs2(nx,ny)

            elif arr[nx][ny] != 0 : # 얼음이라면
                if arr[nx][ny] == 99 : # 단, 녹은 곳은 아님.
                    continue
                arr[nx][ny] -= 1
                if arr[nx][ny] <= 0:
                    arr[nx][ny] = 99


            
def dfs1(x,y):      # 분단 여부판단
    
    visited[x][y] = 7
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 4 :
            if arr[nx][ny] != 0 :   # 빙산이라면
                dfs1(nx,ny)

            


while(True):

    for i in range(r):
        print(arr[i])
    print()

    think = 0   # 빙산의 분단 여부판단
    visited = [[4]*c for _ in range(r)] # 4 미방문 , 7 방문

    

    # 빙산 분단 여부 확인 구역
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and visited[i][j] == 4:
                dfs1(i,j)
                think += 1

    if think == 0 :     # 얼음이 없다면.
        print('0')
        break # 종료
    if think >= 2 :
        print(answer)
        break

    ##################################

    answer += 1


    # 빙산 녹이는 양 구하기

    
    visited = [[4]*c for _ in range(r)] # 4 미방문 , 7 방문

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0 and visited[i][j] == 4 : # 물이고 방문하지 않은 
                dfs2(i,j)




    for i in range(r):
        for j in range(c):
            if arr[i][j] == 99 :
                arr[i][j] = 0









    
