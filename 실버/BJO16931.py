# 크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다. 이 종이의 각 칸 위에 1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.

# 종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.



# 위의 그림은 3×3 크기의 종이 위에 정육면체를 놓은 것이고, 겉넓이는 60이다.

import sys

N,M = map(int,sys.stdin.readline().split())

graph = []

for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))


max_side = []
max_front = []

for i in range(N):
    max_s = graph[i][0]
    for j in range(1,M):
        if graph[i][j] - graph[i][j-1] > 0:
            max_s += graph[i][j] - graph[i][j-1]
    max_side.append(max_s)


for j in range(M):
    max_f = graph[0][j]
    for i in range(1,N):
        if graph[i][j] - graph[i-1][j] > 0:
            max_f += graph[i][j] - graph[i-1][j]
    max_front.append(max_f)




print(N*M*2+sum(max_side*2)+sum(max_front)*2)