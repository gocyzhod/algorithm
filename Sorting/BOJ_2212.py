import sys

input = sys.stdin.readline

# 16:05

# k 개의 집중국
# n : 센서의 개수, k = 집중국의 개수
# arr = n개 센서의 좌표

n = int(input())

k = int(input())

arr = list(map(int,input().split()))
arr.sort()

tmp = []

for i in range(1, len(arr)):
    tmp.append(arr[i]-arr[i-1])
tmp.sort()
answer = 0
for i in range(len(tmp)-(k-1)):
    
    answer+=tmp[i]
print(answer)
