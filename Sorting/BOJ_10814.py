import sys
N = int(sys.stdin.readline())

arr = [[0]*3 for _ in range(N)]

for i in range(N):
    a, b = sys.stdin.readline().split()
    arr[i][0] = int(a)
    arr[i][1] = b
    arr[i][2] = i+1

arr = sorted(arr, key = lambda arr : ( arr[0], arr[2]))

#print(arr)

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])
