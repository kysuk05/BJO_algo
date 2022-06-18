# 상근이는 오른쪽 그림과 같은 지도에서 진행하는 게임을 만들었다.

# 지도는 총 2개의 줄로 나누어져 있으며, 각 줄은 N개의 칸으로 나누어져 있다. 칸은 위험한 칸과 안전한 칸으로 나누어져 있고, 안전한 칸은 유저가 이동할 수 있는 칸, 위험한 칸은 이동할 수 없는 칸이다.

# 가장 처음에 유저는 왼쪽 줄의 1번 칸 위에 서 있으며, 매 초마다 아래 세 가지 행동중 하나를 해야 한다.

# 한 칸 앞으로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i+1번 칸으로 이동한다.
# 한 칸 뒤로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i-1번 칸으로 이동한다.
# 반대편 줄로 점프한다. 이때, 원래 있던 칸보다 k칸 앞의 칸으로 이동해야 한다. 예를 들어, 현재 있는 칸이 왼쪽 줄의 i번 칸이면, 오른쪽 줄의 i+k번 칸으로 이동해야 한다.
# N번 칸보다 더 큰 칸으로 이동하는 경우에는 게임을 클리어한 것이다.

# 게임을 재밌게 하기 위해서, 상근이는 1초에 한 칸씩 각 줄의 첫 칸이 사라지는 기능을 만들었다. 즉, 게임을 시작한지 1초가 지나면 1번 칸이 사라지고, 2초가 지나면 2번 칸이 사라진다. 편의상 유저가 먼저 움직이고, 칸이 사라진다고 가정한다. 즉, 이번에 없어질 칸이 3번 칸인데, 상근이가 3번 칸에 있다면, 3번 칸에서 다른 칸으로 이동하고 나서 3번 칸이 없어지는 것이다.

# 각 칸의 정보가 주어졌을 때, 게임을 클리어 할 수 있는지, 없는지 구하는 프로그램을 작성하시오.

import sys
from collections import deque

N,k = map(int,sys.stdin.readline().split())

graph = []
for i in range(2):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)
check = [[0 for i in range(N)] for i in range(2)]

qu = deque()
qu.append((0,0))
check[0][0] = 1

ans = 0
while qu:
    x,y = qu.popleft()
    for i in range(3):
        if i == 0:
            dx = x
            dy = y+1
        elif i == 1:
            dx = x
            dy = y-1
        elif i == 2:
            if x == 1:
                dx = x-1
            else:
                dx = x+1
            dy = y+k
        
        if dy < 0:
            continue
        if dy >= N:
            ans = 1
            break
        if graph[dx][dy] == '0':
            continue
        if check[dx][dy] != 0:
            continue
        if check[x][y] > dy:
            continue
        check[dx][dy] = check[x][y] + 1
        qu.append((dx,dy))
print(ans)