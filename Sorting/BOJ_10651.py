import sys
N = int(sys.stdin.readline())
arr = [[0]*2  for _ in range(N)]

for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    arr[i][0] = a
    arr[i][1] = b

arr = sorted(arr , key = lambda arr : (arr[1],arr[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])
