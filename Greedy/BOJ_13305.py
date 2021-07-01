## 14시 30분 시작
## 13305 주우소 gready

import  sys

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int,input().split()))

del price[len(price)-1]

Sum = road[0]*price[0]
current_price = price[0]

i = 0

for i in range(1, len(road)):
    if current_price <= price[i]:
        Sum += road[i]*current_price
    elif current_price > price[i] :
        Sum += road[i]*price[i]
        current_price = price[i]
print(Sum)


문제 해설 :
전형적인 그리디 문제이다.
 A B C 라는 곳이 있다고 해보자
우선 처음 출발할 때는 A에서는 무조건 주유를 하여야한다.
그 후 다음 B 도시가 저렴하면 B->C 를 갈 기름을 B 도시에서 주유를 한다.
그 후 다음 B 도시가 비싸면 B->C 를 갈 기름만큼을 A도시에서 추가로 주유한다.
즉 다음 도시에서 더 저렴한 기름값이 발견되기 전까지 그 전의 도시에서 저렴한 기름값을 주유하면 된다.
