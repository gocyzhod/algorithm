import sys
arr = [0]*10001
N = int(sys.stdin.readline())
for i in range(N):
    input_num = int(sys.stdin.readline())

    arr[input_num-1] = arr [input_num-1] +1
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
