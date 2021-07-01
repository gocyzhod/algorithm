import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * (N+2)


arr[0] = 0
arr[1] = 1
for i in range(2,N+2):
    arr[i] = (arr[i-1] + arr[i-2])%15746
    

if N== 0:
    print(0)
else:
    print(arr[N+1])
