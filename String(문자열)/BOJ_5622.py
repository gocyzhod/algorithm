import sys

input = sys.stdin.readline

text = input().lower()

dial = ['abc','def','ghi','jkl' ,'mno','pqrs','tuv','wxyz']
count=[]

for i in text:
    for j in range(len(dial)):
        for k in range(len(dial[j])):
            if i == dial[j][k]:
                count.append(3+j)

print(sum(count))
