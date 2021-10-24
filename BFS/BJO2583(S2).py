# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 
# 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 
# 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.
# 예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 
# 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

# <그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, 
# K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
# 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.


import sys
from collections import deque

m,n,k = map(int,sys.stdin.readline().split())
graph = [[0 for a in range(n)]for b in range(m)]
queue = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[y][x] = '1'

stack = []
def bfs():
    area = 1
    while queue:
        x,y = queue.popleft()
        graph[x][y] = '1'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny>=n:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = '1'
                area+=1
                queue.append((nx,ny))
    return(area)

for a in range(m):
    for b in range(n):
        if graph[a][b] == 0:
            queue.append((a,b))
            k = bfs()
            if k:
                stack.append(k)
stack.sort()
print(len(stack))
for n in range(len(stack)):
    print(stack[n],end=' ')



