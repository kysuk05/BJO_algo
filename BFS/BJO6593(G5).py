# 당신은 상범 빌딩에 갇히고 말았다. 
# 여기서 탈출하는 가장 빠른 길은 무엇일까? 
# 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 
# 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 
# 당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 
# 즉, 대각선으로 이동하는 것은 불가능하다. 
# 그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.

# 당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어지며, 각 테스트 케이스는 세 개의 정수 L, R, C로 시작한다. L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다. R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수를 나타낸다.

# 그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다. 
# 각 문자는 상범 빌딩의 한 칸을 나타낸다. 
# 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 
# 비어있는 칸은 '.'으로 표현된다. 
# 당신의 시작 지점은 'S'로 표현되고, 
# 탈출할 수 있는 출구는 'E'로 표현된다. 
# 각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현된다. 
# 시작 지점과 출구는 항상 하나만 있다.



import sys
from collections import deque

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

def bfs():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or nx>=c or ny<0 or ny>=r or nz<0 or nz>=l:
                continue
            if graph[nz][ny][nx] not in ('.','E'):
                continue
            if graph[nz][ny][nx] == 'E':
                return (graph[z][y][x]+1)
            if graph[nz][ny][nx] == '.':
                graph[nz][ny][nx] = graph[z][y][x]+1
                queue.append((nz,ny,nx))


while True:
    graph = []
    graph2 = []
    queue = deque()
    l,r,c = map(int,sys.stdin.readline().split())
    if l==0 and r==0 and c==0:
        break
    else:
        for i in range(l):
            for j in range(r):
                graph2.append(list(''.join(sys.stdin.readline().rstrip())))
            space = sys.stdin.readline()
            graph.append(graph2)
            graph2 = []
        
        for e in range(c):
            for f in range(r):
                for g in range(l):
                    if graph[g][f][e] == 'S':
                        queue.append((g,f,e))
                        graph[g][f][e] = 0
                        k = bfs()
        if k:
            print('Escaped in',k,'minute(s).')
        else:
            print('Trapped!')