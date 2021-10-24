# 여러 섬으로 이루어진 나라가 있다. 
# 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다. 
# 하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다. 
# 그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 
# 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

# 이 나라는 N×N크기의 이차원 평면상에 존재한다. 
# 이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 
# 다음은 세 개의 섬으로 이루어진 나라의 지도이다.
# 위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 
# 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 
# 가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 
# 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.


# 물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 
# 위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).
# 지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

# 아이디어를 떠올리는데 많은 시행착오가 있었던 문제.
# 시간이 많이 걸렸다.
import sys
from collections import deque
import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]
n = int(sys.stdin.readline())
graph = []
queue = deque()
check = list(list((True)for a in range(n))for b in range(n))
que2 = copy.deepcopy(queue)
chnum = 2
for i in range(n):
    graph.append(list(sys.stdin.readline().split()))


# 먼저 섬마다 번호를 매긴다.
def che():
    while que2:
        x,y = que2.popleft()
        check[x][y] = chnum
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if check[nx][ny] != True:
                continue
            if graph[nx][ny] != '1':
                continue
            if graph[nx][ny] == '1':
                check[nx][ny] = chnum
                que2.append((nx,ny))

for a in range(n):
    for b in range(n):
        if graph[a][b] == '1' and check[a][b] == True:
            que2.append((a,b))
            che()
            chnum+=1


ans = []
# bfs를 실행 해서 만약 번호가 다른 섬을 만나면 거리 값을 리턴하려고 한다.
# 단 거리가 짝수인 경우 리턴을 못하는 경우가 생긴다.
# 따라서 모든 만나는 값을 ans스택에 저장하고 최솟값을 출력한다.
def bfs():
    while queue:
        x,y = queue.popleft()
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if check[nx][ny] == check[x][y]:
                continue
            
            if (check[nx][ny] != True) and check[x][y] != check[nx][ny]:
                if graph[x][y] == '1':
                    ans.append(graph[nx][ny])
                elif graph[nx][ny] == '1':
                    ans.append(graph[x][y])
                else:
                    ans.append(graph[x][y]+graph[nx][ny])
            
            if check[nx][ny] == True:
                check[nx][ny] = check[x][y]
                if graph[x][y] == '1':
                    graph[nx][ny] = 1
                else:
                    graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            queue.append((i,j))

bfs()
print(min(ans))
