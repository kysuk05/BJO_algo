# 사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

# 티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

# 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

# 티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다. 


import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    t = sys.stdin.readline().rstrip()
    graph.append(list(t))


w_qu = deque()
s_qu = deque()
ix = [1,0,-1,0]
iy = [0,1,0,-1]

check = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            w_qu.append((i,j))
            check[i][j] = 1
        elif graph[i][j] == 'S':
            s_qu.append((i,j))
            check[i][j] = 1
ans = []

def bfs():
    global ans
    while s_qu:
        if w_qu and s_qu:
            if check[w_qu[0][0]][w_qu[0][1]] <= check[s_qu[0][0]][s_qu[0][1]]:
                x,y = w_qu.popleft()
                for i in range(4):
                    dx = x+ix[i]
                    dy = y+iy[i]
                    if dx >= n or dy >= m or dx<0 or dy <0:
                        continue
                    if graph[dx][dy] in ('D','X'):
                        continue
                    if check[dx][dy] != 0:
                        continue
                    graph[dx][dy] = '*'
                    check[dx][dy] = check[x][y] + 1
                    w_qu.append((dx,dy))
            else:
                x,y = s_qu.popleft()
                for i in range(4):
                    dx = x+ix[i]
                    dy = y+iy[i]
                    if dx >= n or dy >= m or dx < 0 or dy <0:
                        continue
                    if graph[dx][dy] == 'D':
                        ans.append(check[x][y])
                        continue
                    if graph[dx][dy] in ('*','X'):
                        continue
                    if check[dx][dy] != 0:
                        continue
                    graph[dx][dy] = 'S'
                    check[dx][dy] = check[x][y] + 1
                    s_qu.append((dx,dy))
        
        elif s_qu:
            x,y = s_qu.popleft()
            for i in range(4):
                dx = x+ix[i]
                dy = y+iy[i]
                if dx >= n or dy >= m or dx < 0 or dy <0:
                    continue
                if graph[dx][dy] == 'D':
                    ans.append(check[x][y])
                    continue
                if graph[dx][dy] in ('*','X'):
                    continue
                if check[dx][dy] != 0:
                    continue
                graph[dx][dy] = 'S'
                check[dx][dy] = check[x][y] + 1
                s_qu.append((dx,dy))

bfs()
if not ans:
    print('KAKTUS')
else:
    print(min(ans))