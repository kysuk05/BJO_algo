# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다)  이동한다. 
# 불은 각 지점에서 네 방향으로 확산된다. 
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다. 
# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

#  각각의 문자들은 다음을 뜻한다.

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.

import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
graph = []
for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

fqueue = deque()
jqueue = deque()
def bfs():
    while fqueue or jqueue:
        if fqueue:
            for fi in range(len(fqueue)):
                fx,fy = fqueue.popleft()
                for i in range(4):
                    #불
                    nfx = fx+dx[i]
                    nfy = fy+dy[i]
                    if nfx<0 or nfx>=r or nfy<0 or nfy>=c:
                        continue
                    if graph[nfx][nfy] != '.':
                        continue
                    if graph[nfx][nfy] == '.':
                        graph[nfx][nfy] = '#'
                        fqueue.append((nfx,nfy))
        for ji in range(len(jqueue)):
            jx,jy = jqueue.popleft()
            if ((jx==0) or (jy==0) or (jx==r-1) or (jy ==c-1)):
                return(graph[jx][jy])
            for i in range(4):
                #지훈
                njx = jx+dx[i]
                njy = jy+dy[i]
                if njx<0 or njx>=r or njy<0 or njy>=c:
                    continue
                if graph[njx][njy] == '#':
                    continue
                if graph[jx][jy] != '#' and graph[njx][njy] == '.':
                    graph[njx][njy] = graph[jx][jy]+1
                    jqueue.append((njx,njy))

for k in range(r):
    for l in range(c):
        if graph[k][l] == 'J':
            graph[k][l] = 1
            jihun = (k,l)
        elif graph[k][l] == 'F':
            fire = (k,l)
            fqueue.append(fire)
jqueue.append(jihun)

k = bfs()

if k:
    print(k)
else:
    print('IMPOSSIBLE')