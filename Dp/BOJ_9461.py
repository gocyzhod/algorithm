# 16시 40분 시작

import sys
input = sys.stdin.readline

testcase = int(input())

question = []

dp = [0]*(102)
dp[0] = 0
dp[1],dp[2],dp[3] = 1,1,1
dp[4],dp[5] = 2,2
dp[6] = 3
dp[7] = 4
dp[8] = 5
for i in range(9,102):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(testcase):
    question.append(int(input()))
for i in range(len(question)):
    print(dp[question[i]])
