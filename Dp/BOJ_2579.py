import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(10):
    arr.append(0)

dp = [0] * (n+10)
dp[0] = arr[0] # 20
dp[1] = arr[0] + arr[1] # 30
dp[2] = max ( arr[0] + arr[2] , arr[1] + arr[2] )

if n >= 3 :
    for i in range(3, n+3):
        dp[i] = max ( dp[i-3] + arr[i-1] + arr[i] , dp[i-2] + arr[i] )
        #print(dp[i])

print((dp[n-1]))
