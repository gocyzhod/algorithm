import sys
input = sys.stdin.readline
X =  int(input())

arr = [0] * (X+1)

for i in range(2, X+1):
    arr[i] = arr[i-1]+1
    if i % 3 == 0 :
        arr[i] = min( arr[i//3]+1 , arr[i] )
    if i % 2 == 0 :
        arr[i] = min( arr[i // 2] + 1, arr[i])
print(arr[X])
