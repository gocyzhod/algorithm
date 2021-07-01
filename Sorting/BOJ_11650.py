import sys
N = int(sys.stdin.readline())
arr = [[0]* 2 for i in range(N)]
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    arr[i][0] = a
    arr[i][1] = b
arr.sort()

for i in range(N):
    for j in range(N):
        if arr[i] == arr[j] :
            sorted(arr, key=lambda item: item[1])
for i in range(N):
    print(arr[i][0], arr[i][1])

    
    # 시간초과가 난 코딩
