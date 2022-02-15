# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

# 안전 거리가 가장 큰 칸을 구해보자. 


import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    t = list(map(int,sys.stdin.readline().split()))
    graph.append(t)

check = [[0 for i in range(m)]for j in range(n)]

qu = deque()
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            check[i][j] = 1
            qu.append((i,j))


dx = [-1,-1,-1,0,0,1,1,1]
dy = [1,0,-1,1,-1,1,0,-1]

t = 0
while qu:
    x,y = qu.popleft()
    for i in range(8):
        ix = x+dx[i]
        iy = y+dy[i]
        if ix >= 0 and ix < n and iy >= 0 and iy < m:
            if check[ix][iy] == 0:
                check[ix][iy] = check[x][y] +1
                t = check[ix][iy]
                qu.append((ix,iy))

print(t-1)