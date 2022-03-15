# 게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

# 크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.

# 데스 나이트는 체스판 밖으로 벗어날 수 없다.


import sys
from collections import deque

n = int(sys.stdin.readline())


graph = [[0 for i in range(n)]for j in range(n)]

qu = deque()

x,y,ax,ay = map(int,sys.stdin.readline().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

graph[x][y] = 1
qu.append((x,y))
ans = 0
while qu:
    x,y = qu.popleft()
    if x == ax and y == ay:
        ans = graph[x][y]
        break
    for i in range(6):
        ix = x+dx[i]
        iy = y+dy[i]
        if ix < 0 or ix >= n or iy < 0 or iy >= n:
            continue
        if graph[ix][iy] != 0:
            continue
        graph[ix][iy] = graph[x][y] + 1
        qu.append((ix,iy))

print(ans-1)