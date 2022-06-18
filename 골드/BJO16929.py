# Two Dots는 Playdots, Inc.에서 만든 게임이다. 게임의 기초 단계는 크기가 N×M인 게임판 위에서 진행된다.


# 각각의 칸은 색이 칠해진 공이 하나씩 있다. 이 게임의 핵심은 같은 색으로 이루어진 사이클을 찾는 것이다.

# 다음은 위의 게임판에서 만들 수 있는 사이클의 예시이다.

	
# 점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의는 아래와 같다.

# 모든 k개의 점은 서로 다르다. 
# k는 4보다 크거나 같다.
# 모든 점의 색은 같다.
# 모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 또, dk와 d1도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.
# 게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.

import sys

N,M = map(int,sys.stdin.readline().split())

check = [[0 for i in range(M)]for j in range(N)]
graph =[]

for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)


cycle = []
ix = [1,0,-1,0]
iy = [0,1,0,-1]


def dfs(x,y):
    for k in range(4):
        dx = x+ix[k]
        dy = y+iy[k]
        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue
        if graph[x][y] != graph[dx][dy]:
            continue
        if check[dx][dy] != 0 and check[dx][dy]-check[x][y] >= 3:
            print('Yes')
            exit(0)
        if check[dx][dy] == 0:
            check[dx][dy] = check[x][y] + 1
            dfs(dx,dy)

ans = 'No'
for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            check[i][j] = 1
            dfs(i,j)

print(ans)