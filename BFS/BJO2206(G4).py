# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

#시간초과로 엄청 빡빡했다.
import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(''.join(sys.stdin.readline().rstrip())))


check = [[0 for a in range(m)]for b in range(n)]
ans = [[0 for a in range(m)]for b in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue = deque()

check[0][0] = 1
ans[0][0] = 1
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if (nx == n-1) and (ny == m-1):
                return(ans[x][y]+1)
            
            if check[nx][ny] == 1:
                continue
            
            elif check[nx][ny] == 2:
                if check[x][y] != 1:
                    continue


            if graph[nx][ny] == '0':
                check[nx][ny] = check[x][y]
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx,ny))
            
            elif graph[nx][ny] == '1':
                if check[x][y] == 1:
                    check[nx][ny] = 2
                    ans[nx][ny] = ans[x][y]+1
                    queue.append((nx,ny))
                if check[x][y] == 2:
                    continue

queue.append((0,0))
if n == 1 and m == 1:
    print(1)
else:
    ans = bfs()
    if ans:
        print(ans)
    else:
        print(-1)