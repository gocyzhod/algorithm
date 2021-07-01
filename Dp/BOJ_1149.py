# 17시 30분 시작

import sys
input = sys.stdin.readline


n = int(input())
color = [[0]*3 for _ in range(n+1)]

for i in range(n):
    r,g,b = map(int,input().split())
    color[i][0] = r
    color[i][1] = g
    color[i][2] = b

for i in range(n):
    color[i][0] = min(color[i-1][1],color[i-1][2]) + color[i][0]
    color[i][1] = min(color[i-1][0],color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0],color[i-1][1]) + color[i][2]
print(min(min(color[n-1][0],color[n-1][1]),color[n-1][2]))
