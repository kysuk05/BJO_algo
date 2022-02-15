# 크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.

# 목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.

import sys
a,b = map(int,sys.stdin.readline().split())

graph = []
for i in range(a):
    li = []
    t = sys.stdin.readline().rstrip()
    for j in t:
        li.append(j)
    graph.append(li)

ix = [-1,0,1,0]
iy = [0,-1,0,1]

check = 0
for i in range(a):
    for j in range(b):
        if graph[i][j] == 'W':
            for n in range(4):
                if i+ix[n] >= 0 and i+ix[n] < a and j+iy[n] >= 0 and j+iy[n] < b:
                    if graph[i+ix[n]][j+iy[n]] == 'S':
                        check = 1
        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if check == 1:
    print('0')
else:
    print('1')
    for i in range(a):
        for j in range(b):
            print(graph[i][j],end='')
        print()