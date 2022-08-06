# 가로 A(1≤A≤100), 세로 B(1≤B≤100) 크기의 땅이 있다. 이 땅 위에 로봇들이 N(1≤N≤100)개 있다.



# 로봇들의 초기 위치는 x좌표와 y좌표로 나타난다. 위의 그림에서 보듯 x좌표는 왼쪽부터, y좌표는 아래쪽부터 순서가 매겨진다. 또한 각 로봇은 맨 처음에 NWES 중 하나의 방향을 향해 서 있다. 초기에 서 있는 로봇들의 위치는 서로 다르다.

# 이러한 로봇들에 M(1≤M≤100)개의 명령을 내리려고 한다. 각각의 명령은 순차적으로 실행된다. 즉, 하나의 명령을 한 로봇에서 내렸으면, 그 명령이 완수될 때까지 그 로봇과 다른 모든 로봇에게 다른 명령을 내릴 수 없다. 각각의 로봇에 대해 수행하는 명령은 다음의 세 가지가 있다.

# L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
# R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
# F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
# 간혹 로봇들에게 내리는 명령이 잘못될 수도 있기 때문에, 당신은 로봇들에게 명령을 내리기 전에 한 번 시뮬레이션을 해 보면서 안전성을 검증하려 한다. 이를 도와주는 프로그램을 작성하시오.

# 잘못된 명령에는 다음의 두 가지가 있을 수 있다.

# Robot X crashes into the wall: X번 로봇이 벽에 충돌하는 경우이다. 즉, 주어진 땅의 밖으로 벗어나는 경우가 된다.
# Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우이다.

import sys

A,B = map(int,sys.stdin.readline().split())
N,M = map(int,sys.stdin.readline().split())

graph = [[0 for i in range(A)]for i in range(B)]

robot = []

for _ in range(N):
    x,y,t = sys.stdin.readline().split()
    if t == 'W':
        t = 0
    elif t == 'N':
        t = 1
    elif t == 'E':
        t = 2
    elif t == 'S':
        t = 3
    robot.append([int(x)-1,B-int(y),t])
    graph[B-int(y)][int(x)-1] = 1



dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(M):
    r,o,m = sys.stdin.readline().split()
    r = int(r)
    m = int(m)
    if o == 'R':
        robot[r-1][2] = (robot[r-1][2]+m)%4
    elif o == 'L':
        robot[r-1][2] = (robot[r-1][2]-m)%4
    else:
        x = robot[r-1][0]
        y = robot[r-1][1]
        w = robot[r-1][2]
        graph[y][x] = 0
        for i in range(m):
            x += dx[w]
            y += dy[w]
            if y >= B or y < 0 or x >= A or x < 0:
                print('Robot '+str(r)+' crashes into the wall')
                exit()
            elif graph[y][x] != 0:
                for j in range(len(robot)):
                    if robot[j][0] == x and robot[j][1] == y:
                        print('Robot '+str(r)+' crashes into robot '+str(j+1))
                        exit()
        graph[y][x] = 1
        robot[r-1][0] = x
        robot[r-1][1] = y
print('OK')
