import sys
N = int(input())
arr=[[0]*2 for i in range(N)]

for i in range(N):
    k = sys.stdin.readline()
    arr[i][0] = k
for i in range(len(arr)):
    arr[i][1] = len(arr[i][0])

#중복제거
for i in range(len(arr)):
    arr[i] = tuple(arr[i])
arr = set(arr)

arr = sorted(arr, key = lambda arr: (arr[1],arr[0]))


for i in range(len(arr)):
    print(arr[i][0], end='')
