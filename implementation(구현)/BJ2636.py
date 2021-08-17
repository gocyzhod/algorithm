## 15 start

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

r,c = map(int,input().split())

answer = 0

arr = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(r):
    tmp = list(map(int,input().split()))

    arr.append(tmp)


def dfs(x,y):
    visited[x][y] = 7       # 방문처리 해주고
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 4 :   # 범위 내 이고 방문하지 않았다면
            if arr[nx][ny] == 0 :   # 빈 공간이라면
                dfs(nx,ny)          # 다시 dfs
            elif arr[nx][ny] == 1 : # 만약 빙산이라면
                visited[nx][ny] = 0 # 빙산을 녹인것으로 기억만 시키기.
            

answer_ice = []

while(True):
    ice = 0
    
    visited = [[4] * c for _ in range(r)]
    # 4 미방문, 7 방문처리

    think = 0

    
    for i in range(r):
        ice += arr[i].count(1)    # 얼음이 있다면

    answer_ice.append(ice)
    if ice == 0:  # 얼음이 없다면.
        break       # 멈춰라

    
    else :

        for i in range(r):
            for j in range(c):
                if i == 0  or j == 0 :   # 벽에 붙어있는 것부터. 즉 얼음 안의 빈 공간이 아니라면,
                    
                    if arr[i][j] == 0 and visited[i][j] == 4:   # 빈 공간이고 방문하지 않았다면
                        dfs(i,j)                                # dfs


    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0 :
                arr[i][j] = 0


    answer += 1

answer_ice.sort()

print(answer)
if len(answer_ice) == 1:
    print('0')
else:
    print((answer_ice[1]))

                    
