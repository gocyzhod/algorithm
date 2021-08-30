import sys
sys.setrecursionlimit(10 ** 6)

def dfs(now, visited, n,computers):

    visited[now] = True
    for computer in range(n) :
        if visited[computer] == False and computers[now][computer] == 1:
            dfs(computer,visited, n,computers)
    
def solution(n, computers):
    answer = 0
    
    # a - b - c
    # a -- c : 간접 연결 , 정보교환 가능
    # a,b,c -- 같은 네트워크
    
    visited = [False] * n
    

    for computer in range(n):
        if visited[computer] == False :
            #print(computer)
            print(visited)
            dfs(computer,visited, n,computers)
            answer+=1
    
    return answer
