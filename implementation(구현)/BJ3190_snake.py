## 15H 시작

import sys
input = sys.stdin.readline


n = int(input())
k = int(input())

Map = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):

    applex, appley = map(int,input().split())

    Map[applex-1][appley-1] = 5 # 사과존재 구역


L = int(input()) # 뱀의 방향

order=[]

for i in range(L):
    x,c = input().split()
    order.append([x,c])

Map[0][0] = 7    # 처음 뱀 위치
snakex = 0
snakey = 0  # 기존 뱀의 위치

cnt = 0     # 움직인 횟수 카운트
ordercnt = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]     # 아래, 오른쪽, 위, 왼쪽
way = 1 # 기본은 오른쪽을 향한다.

lastplace = []
lastplace.append([0,0])
place = 0

thinkx = 0
thinky = 0

while(True):
    
    
    cnt += 1

    

    snakex += dx[way]
    snakey += dy[way]

    if snakex > 0 :
        thinkx = 1
    if snakey > 0 :
        thinky = 1


    if Map[snakex][snakey] == 7 : # 다음 장소가 뱀의 몸통이라면, 멈춰라
        break
        
    elif Map[snakex][snakey] == 5 : # 사과가 있다면
        Map[snakex][snakey] = 7 # 뱀 길이 연장

        lastplace.append([snakex,snakey]) # 뱀의 위치들을 기억

    elif Map[snakex][snakey] != 5 : # 사과가 없다면
        #for i in range(n+1):
        #    print(Map[i])
       # print()
        Map[snakex][snakey] = 7 # 뱀을 다음칸으로 이동, 단 맨뒷 꼬리 삭제

        #for i in range(n+1):
         #   print(Map[i])
        #print(cnt)
            
        lastplace.append([snakex,snakey])
            
        Map[lastplace[place][0]][lastplace[place][1]] = 0 # 뱀의 맨뒷꼬리를 삭제
    
                    
        place += 1

    if int(order[ordercnt][0]) == cnt : # 움직이고 난 후, 방향을 바꾼다면.
        if order[ordercnt][1] == 'L' :
            way += 1
            if way == 4 :
                way = 0

        if order[ordercnt][1] == 'D' :
            way -= 1
            if way == -1 :
                way = 3
                
        if ordercnt < L-1 :
            ordercnt += 1


    if snakex  >= n or snakey  >= n : # 벽이라면
        #print('1')
        break # Stop
    if thinkx == 1 and snakex < 0 :
     #   print('2')
        break
    if thinky == 1 and snakey < 0 :
      #  print('3')
        break

    #for i in range(10):
     #   print(Map[i])
        
    #print()
print(cnt)
