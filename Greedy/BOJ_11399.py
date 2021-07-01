import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split())) # 각 사람들이 걸린 시간.

arr.sort()

Sum = 0
Sum_arr = []
result = 0

for i in range(len(arr)):
    Sum = arr[i] + Sum
    Sum_arr.append( Sum )

print(sum(Sum_arr))
