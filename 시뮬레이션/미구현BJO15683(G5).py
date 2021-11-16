# 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 
# 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

# CCTV의 최대 개수는 8개를 넘지 않는다.

import sys
from copy import deepcopy
n,m = map(int,sys.stdin.readline().split())
lis1 = []
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def fun1(graph,k):
    x,y = lis1.pop()
    graph[x][y] = 1
    if k == 0:
        nx = x
        while nx >= 0:
            if graph[nx][y] == 6:
                break
            graph[nx][y] = '1'
            nx -= 1
    elif k == 1:
        nx = x
        while nx < n:
            if graph[nx][y] == 6:
                break
            graph[nx][y] = '1'
            nx += 1
    elif k == 2:
        ny = y
        while ny >= 0:
            if graph[x][ny] == 6:
                break
            graph[x][ny] = '1'
            ny -= 1
    elif k == 3:
        ny = y
        while ny < m:
            if graph[x][ny] == 6:
                break
            graph[x][ny] = '1'
            ny += 1
    return graph


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            for k in range(4):
                gr1 = deepcopy(graph)
                lis1.append((i,j))
                print(fun1(gr1,k))
