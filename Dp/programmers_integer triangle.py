# 13 : 13 start

def solution(triangle):
    answer = 0
    
    ll = len(triangle)
    dp = []
    
    for i in triangle:
        i.insert(0,0)
        i.append(0)
    
    for i in range(1, ll):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] += max( triangle[i-1][j-1] , triangle[i-1][j]  )
    
    answer = max(triangle[ll-1])
    
    return answer


"""

삼각형의 triangle 리스트 맨앞과 맨 뒤에 0 인덱스 값을 추가하여준다.
그 후, 위에서 아래로 더해나간다.

맨 마지막 리스트들 중 가장 큰 값을 리턴하여준다.

"""
