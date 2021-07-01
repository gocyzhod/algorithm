import sys

input = sys.stdin.readline

num_1 , num_2 = input().split()
num_1 = num_1[::-1]
num_2 = num_2[::-1]

if num_1 > num_2:
    print(num_1)
else:
    print(num_2)
