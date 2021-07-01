import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    a,b = input().split()
    text = ''
    for i in b :
        text += int(a) * i
    print(text)
