# 크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며, 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다. 

#   2
# 4 1 3
#   5
#   6
# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

# 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.


import sys

N,M,x,y,k = map(int,sys.stdin.readline().split())

graph = []

for i in range(N):
    t = list(map(int,sys.stdin.readline().split()))
    graph.append(t)

roll = list(map(int,sys.stdin.readline().split()))
dice = [0,0,0,0,0,0]
# F B L R U D

def right():
    tem = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = dice[4]
    dice[4] = tem
    print(dice[4])

def left():
    tem = dice[2]
    dice[2] = dice[4]
    dice[4] = dice[3]
    dice[3] = dice[5]
    dice[5] = tem
    print(dice[4])

def up():
    tem = dice[0]
    dice[0] = dice[5]
    dice[5] = dice[1]
    dice[1] = dice[4]
    dice[4] = tem
    print(dice[4])

def down():
    tem = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[1]
    dice[1] = dice[5]
    dice[5] = tem
    print(dice[4])

for i in range(k):
    if roll[i] == 1:
        if y < M-1:
            y += 1
            right()
            
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
    elif roll[i] == 2:
        if y > 0:
            y -= 1
            left()
            
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
    elif roll[i] == 3:
        if x > 0:
            x -= 1
            up()
            
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
    elif roll[i] == 4:
        if x < N-1:
            x += 1
            down()
            
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0