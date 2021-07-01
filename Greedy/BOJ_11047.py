#준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한
#동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
point = 0
coin = []
count = 0

for i in range(N):
    a = int(input())
    coin.append(a)

for i in range(N- 1 , -1 , -1):
    if K == 0:
        break
    if coin[i] > K:
        continue
    count += K // coin[i]
    K %= coin[i]
print(count)
