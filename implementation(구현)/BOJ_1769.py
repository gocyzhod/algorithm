import sys

input = sys.stdin.readline

number = list((input().rstrip()))

cnt = 0

tmp = ''.join(number)

answer = []

while(True):
    number = 0
    if len(tmp) == 1:
        break

    for i in range(len(tmp)):
        number += int(tmp[i])

    tmp = str(number)

    
    cnt += 1

answer.append(cnt)
if int(tmp) % 3 != 0 :
    answer.append('NO')
else :
    answer.append('YES')

for i in range(2):
    print(answer[i])
