## 새벽 1시 30분 시작

import sys

input = sys.stdin.readline

alpha = input()

test = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 8개

for t in test:
    alpha = alpha.replace(t,'a')
print(len(alpha)-1)
