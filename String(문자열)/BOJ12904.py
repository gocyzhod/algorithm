import sys

input = sys.stdin.readline

# s, t   s -> t

# 문자열 뒤에 A 추가
# 문자열 뒤집고 뒤에 B 추가


dp = []

S = list(input().rstrip())
T = list(input().rstrip())

while True:
    if len(S) == len(T):
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B' :
        T.pop()
        T = T[::-1]

if S == T :
    print(1)
else :
    print(0)
