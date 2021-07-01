import sys
#import collections import deque
import sys
input = sys.stdin.readline


def dfs(v):
    global cnt
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i] == 0 and adj[v][i] == 1:
            dfs(i)
            cnt+=1
    



n = int(input())
m = int(input())
adj = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]
cnt = 0
for i in range(m):
    x,y = map(int,input().split())
    adj[x][y] = 1
    adj[y][x] = 1

dfs(1)
print(cnt)
