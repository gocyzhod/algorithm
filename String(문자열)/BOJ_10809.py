import sys

input = sys.stdin.readline

name = list(input())
name_list = [[0] * 2 for _ in range(26)]
start = 0

for i in range(len(name)):
    for j in range(i+1,len(name)):
        if name[i] == name[j] :
            name[j] = i+j

for i in range(97,123):
    name_list[start][0] = chr(i)
    name_list[start][1] = -1
    start+=1
    
for i in range(len(name)-1):
    for j in range(len(name_list)):
        if name[i] == name_list[j][0] :
            name_list[j][1] = int(name_list[j][1])
            name_list[j][1] = i

for i in range(len(name_list)):
    print(name_list[i][1], end = ' ')
