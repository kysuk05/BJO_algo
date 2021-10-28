# 동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 
# 그 녀석은 말(Horse)이 되기를 간절히 원했다. 
# 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 
# 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 
# 다음 그림에 말의 이동방법이 나타나있다. 
# x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.

#  	x	 	x	 
# x	 	 	 	x
#  	 	말	 	 
# x	 	 	 	x
#  	x	 	x	 
# 근데 원숭이는 한 가지 착각하고 있는 것이 있다. 
# 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 
# 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.

# 이제 원숭이는 머나먼 여행길을 떠난다. 
# 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다. 
# 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다. 
# 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.




import sys
from collections import deque

queue = deque()

k = int(sys.stdin.readline())
w,h = map(int,sys.stdin.readline().split())

check = [['0' for a in range(w)]for b in range(h)]

graph = []
for i in range(h):
    graph.append(list(sys.stdin.readline().split()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

hx = [2,2,1,1,-1,-1,-2,-2]
hy = [1,-1,2,-2,2,-2,1,-1]
check[0][0] = (1,0)
graph[0][0] = 0

queue.append((0,0))

def bfs():
    while queue:
        x,y = queue.popleft()
        if x == h-1 and y == w-1:
            return(check[x][y][1])
        
        else:
            if graph[x][y] < k:
                for j in range(8):
                    nx = x+hx[j]
                    ny = y+hy[j]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        continue
                    if check[nx][ny] != '0':
                        if graph[nx][ny] <= graph[x][y]+1:
                            continue
                        else:
                            graph[nx][ny] = graph[x][y]+1
                            check[nx][ny] = (1,check[x][y][1]+1)
                            queue.append((nx,ny))
                    if graph[nx][ny] == '0':
                        graph[nx][ny] = graph[x][y] +1
                        check[nx][ny] = (1,check[x][y][1]+1)
                        queue.append((nx,ny))
                
                for l in range(4):
                    nx = x+dx[l]
                    ny = y+dy[l]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        continue
                    if check[nx][ny] != '0':
                        if graph[nx][ny] <= graph[x][y]:
                            continue
                        else:
                            graph[nx][ny] = graph[x][y]
                            check[nx][ny] = (1,check[x][y][1]+1)
                            queue.append((nx,ny))
                    if graph[nx][ny] == '0':
                        graph[nx][ny] = graph[x][y]
                        check[nx][ny] = (1,check[x][y][1]+1)
                        queue.append((nx,ny))
            else:
                for l in range(4):
                    nx = x+dx[l]
                    ny = y+dy[l]
                    if nx<0 or nx>=h or ny<0 or ny>=w:
                        continue
                    if check[nx][ny] != '0':
                        if graph[nx][ny] <= graph[x][y]:
                            continue
                        else:
                            graph[nx][ny] = graph[x][y]
                            check[nx][ny] = (1,check[x][y][1]+1)
                            queue.append((nx,ny))
                    if graph[nx][ny] == '0':
                        graph[nx][ny] = graph[x][y]
                        check[nx][ny] = (1,check[x][y][1]+1)
                        queue.append((nx,ny))

k = bfs()
if w == 1 and h == 1:
    print(0)
else:
    if k:
        print(k)
    else:
        print(-1)