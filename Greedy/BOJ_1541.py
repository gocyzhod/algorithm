a = input().split('-')

num = []

for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1,len(num)):
    n -= num[i]

print(n)


처음에 문제를 보고 어떻게 풀까 고민을 하였다.
우선 문제에서 ' - ' 기호가 키포인트인 것 같았다. 그래서 - 를 기준으로 끊어 입력을 받는다.
그 후 입력받은 문자들 중에서 +를 기준으로 자른다.
그 숫자들을 num 리스트에 넣는다. 그 후 계산.
