# N×N 게임판에 수가 적혀져 있다. 이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.

# 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다. 0은 더 이상 진행을 막는 종착점이며, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다. 한 번 점프를 할 때, 방향을 바꾸면 안 된다. 즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

# 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

import sys
from collections import deque

n = int(sys.stdin.readline())

lis = []

for i in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    lis.append(li)


check = [[0 for i in range(n)]for j in range(n)]
check[0][0] = 1

for i in range(n):
    for j in range(n):
        if lis[i][j] == 0:
            continue
        x = lis[i][j]+i
        if x < n:
            check[x][j] += check[i][j]
        
        y = lis[i][j] + j
        if y < n:
            check[i][y] += check[i][j]
        
        

print(check[-1][-1])

