# 보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.



# 예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.



# 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

import sys

from collections import deque
n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    t = sys.stdin.readline().rstrip()
    graph.append(list(t))


qu = deque()
ix = [1,0,-1,0]
iy = [0,1,0,-1]

last = []
ans = []
def bfs():
    while qu:
        x,y = qu.popleft()
        for i in range(4):
            dx = x+ix[i]
            dy = y+iy[i]
            
            if dx>=n or dy>=m or dx<0 or dy <0:
                continue
            if check[dx][dy] != 0:
                continue
            if graph[dx][dy] == 'W':
                continue
            check[dx][dy] = check[x][y]+1
            qu.append((dx,dy))
            ans.append(check[dx][dy])
        


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            check = [[0 for i in range(m)]for j in range(n)]
            check[i][j] = 1
            qu.append((i,j))
            bfs()

print(max(ans)-1)