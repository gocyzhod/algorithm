#89

#  13:05  start

import sys

input = sys.stdin.readline


n,m = map(int,input().split()) # A에 대한 행렬
a = [list(map(int,input().split())) for i in range(n)]
#for i in range(n):
#    for j in range(m):
        

n,m=map(int,input().split())
b = [list(map(int,input().split())) for i in range(n)]

result = [[0]*len(a) for i in range(len(b[0]))]
x,y = 0,0

def cal(a,b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = a[i][j] * b[j][i]
    return result

print(cal(a,b))
