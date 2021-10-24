# 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.

# 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.

# 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.



# BJO 4179번 불! 문제 풀이에서 알고리즘을 그대로 들고왔다.
import sys
from collections import deque

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
                    if nfx<0 or nfx>=c or nfy<0 or nfy>=r:
                        continue
                    if graph[nfx][nfy] != '.':
                        continue
                    if graph[nfx][nfy] == '.':
                        graph[nfx][nfy] = '*'
                        fqueue.append((nfx,nfy))
        for ji in range(len(jqueue)):
            jx,jy = jqueue.popleft()
            if ((jx==0) or (jy==0) or (jx==c-1) or (jy ==r-1)):
                return(graph[jx][jy])
            for i in range(4):
                #지훈
                njx = jx+dx[i]
                njy = jy+dy[i]
                if njx<0 or njx>=c or njy<0 or njy>=r:
                    continue
                if graph[njx][njy] == '#' or graph[njx][njy] == '*':
                    continue
                if graph[jx][jy] != '#' and graph[njx][njy] == '.':
                    graph[njx][njy] = graph[jx][jy]+1
                    jqueue.append((njx,njy))

t = int(sys.stdin.readline())

for n in range(t):
    r,c = map(int,sys.stdin.readline().split())
    graph = []
    for i in range(c):
        graph.append(list(sys.stdin.readline().rstrip()))
    for k in range(c):
        for l in range(r):
            if graph[k][l] == '@':
                graph[k][l] = 1
                jihun = (k,l)
            elif graph[k][l] == '*':
                fire = (k,l)
                fqueue.append(fire)
    jqueue.append(jihun)
    
    k = bfs()
    if k:
        print(k)
    else:
        print('IMPOSSIBLE')
    jqueue = deque()
    fqueue = deque()