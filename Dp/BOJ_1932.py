# 17시 30분 시작

import sys
input = sys.stdin.readline

n = int(input())

num = []

for i in range(n):
    num.append(list(map(int,input().split())))
    num[i].append(0)
    num[i].insert(0,0)


for i in range(1,n):
    for j in range(1,len(num[i])-1):
        num[i][j] = max( num[i-1][j] + num[i][j] , num[i-1][j-1] + num[i][j] )

print(max(num[n-1]))
