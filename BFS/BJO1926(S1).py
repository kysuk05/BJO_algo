# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 
# 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
# 그림의 넓이란 그림에 포함된 1의 개수이다.

# 입력
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. 
# (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)


import sys
from collections import deque

ans = []
def bfs(x,y):
    num = 0
    queue = deque()
    if graph[x][y] == 1:
        queue.append([x,y])
        graph[x][y] = 0
        num +=1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= a or ny < 0 or ny >= b:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx,ny])
                    num +=1
    if num != 0:
        ans.append(num)
                
                



a, b = map(int,sys.stdin.readline().split())

graph = []

for i in range(a):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [0,-1,1,0]
dy = [-1,0,0,1]

for j in range(a):
    for k in range(b):
        bfs(j,k)

if ans:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)