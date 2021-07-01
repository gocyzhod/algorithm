import sys
input = sys.stdin.readline

N = int(input())

room = [[0]*2 for _ in range(N)]
Num = len(room)
for i in range(N):
    a, b = map(int,input().split())
    room[i][0] = a
    room[i][1] = b


room.sort(key = lambda x : (x[1], x[0]))

count = 1
end_room = room[0][1]

for i in range(1,N):
    if room[i][0] >= end_room:
        count+=1
        end_room = room[i][1]

print(count)



문제 해설 :
이 문제에서는 끝나는 시간과 시작하는 시간이 같을 수가 있다고 조건을 제시하였다.
이 부분을 잘 이해해야한다.
또한 예를 들어
0 11
2 3
3 4
4 5
라고 제시가 주어지면, 23->34->45 라고하여야겠지만, 시작시간을 기준으로 정렬을 한다면 0 11 한가지만 뽑혀 1가지로 답이 나올수도 있다는 점을 유의하여한다.
따라서 0번 인덱스와 1번 인덱스 순으로 정렬을 시켜주면 되는 문제이다.
따라서 lambda를 이용하여 0번 인덱스와 1번 인덱스를 순서대로 정렬을 시켜준다.
