# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
# 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.


import sys
from collections import deque

t = int(sys.stdin.readline())
queue = deque()

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

def bfs(w1,w2):
    while queue:
        x,y = queue.popleft()
        for n in range(8):
            nx = x + dx[n]
            ny = y + dy[n]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                if (nx == w1) and (ny == w2):
                    return graph[x][y]
                else:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx,ny))



for i in range(t):
    l = int(sys.stdin.readline())
    graph = [[0 for a in range(l)]for b in range(l)]
    n1,n2 = map(int,sys.stdin.readline().split())
    queue.append((n1,n2))
    graph[n1][n2] = 1
    w1,w2 = map(int,sys.stdin.readline().split())
    ans = bfs(w1,w2)
    if ans:
        print(ans)
    else:
        print(0)
    queue = deque()