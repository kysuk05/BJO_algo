# 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

# 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.

# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
# M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.

# * 6 5 4 - - 2
# 5 6 - 3 - 0 1
# 4 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 2 2 1 0 1 - -
# 1 - 2 1 2 3 4
# 0 - 3 2 3 4 *
# 시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.

# 0 1 2 3 - - 2
# 1 2 - 3 - 0 1
# 2 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 3 2 1 0 1 - -
# 4 - 2 1 2 3 4
# * - 3 2 3 4 *
# 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.


import sys
from itertools import combinations
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    temp = list(sys.stdin.readline().split())
    graph.append(temp)

empty = 0
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '2':
            virus.append((i,j))
        if graph[i][j] == '0':
            empty += 1
            

ans = sys.maxsize

dx = [-1,0,1,0]
dy = [0,-1,0,1]

act = list(combinations(virus,m))

def bfs(graph):
    global ans
    global empty
    
    t_emp = 0
    m_num = 0
    
    while qu:
        x,y = qu.popleft()
        for i in range(4):
            ix = dx[i] + x
            iy = dy[i] + y
            if ix < 0 or ix >= n or iy < 0 or iy >= n:
                continue
            if che[ix][iy] != 0:
                continue
            if graph[ix][iy] == '2':
                che[ix][iy] = che[x][y]+1
                qu.append((ix,iy))
                continue
            if graph[ix][iy] == '1':
                continue
            if graph[ix][iy] == '0':
                t_emp +=1
                che[ix][iy] = che[x][y] +1
                m_num = max(m_num,che[ix][iy])
                qu.append((ix,iy))
        if t_emp == empty:
            break
    if t_emp == empty:
        ans = min(m_num,ans)


for i in act:
    qu = deque()
    che = [[0 for i in range(n)]for i in range(n)]
    for x,y in i:
        qu.append((x,y))
        che[x][y] = 1
    bfs(graph)

if ans == sys.maxsize:
    print(-1)
elif ans == 0:
    print(0)
else:
    print(ans-1)