import sys

import heapq

input = sys.stdin.readline

n = int(input().rstrip())

q = []
for _ in range(n):
    tmp = list(map(int,input().split()))

    for x in tmp :
        heapq.heappush(q,x)

    while( len(q) > n ):
        heapq.heappop(q)
print(heapq.heappop(q))


"""
heapq 를 사용하는 방법

heapq 의 사용법만 안다면 풀 수 있다.
"""
