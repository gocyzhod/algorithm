import sys

input = sys.stdin.readline

tree = {}
Len = 0

for i in range(1000000):
    name = input().rstrip()
    if name == '' :
        break
    Len += 1
    if name in tree :
        tree[name] += 1
    else :
        tree[name] = 1
    

tree = sorted(tree.items(), key = lambda x:x[0])


for tree_name, tree_num in (tree):
    
    number = round(tree_num / Len , 6) * 100
    print(tree_name, '%.4f' %number )
    

단순히, dict의 활용과 부동소숫점에 대한 이해가 기반이 되면 풀 수 있는 문제이다.
