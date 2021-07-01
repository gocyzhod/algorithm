import sys
input = sys.stdin.readline
a, b , v = map(int,input().split())
result = (v-a) // abs(a-b)
if (v-a) % abs(a-b) != 0:
    result+=1
print(result+1)
