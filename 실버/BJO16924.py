# 십자가는 가운데에 '*'가 있고, 상하좌우 방향으로 모두 같은 길이의 '*'가 있는 모양이다. 십자가의 크기는 가운데를 중심으로 상하좌우 방향으로 있는 '*'의 개수이다. 십자가의 크기는 1보다 크거나 같아야 한다.

# 아래 그림은 크기가 1, 2, 3인 십자가이고, 빈 칸은 '.'이다.

#               ...*...
#       ..*..   ...*...
# .*.   ..*..   ...*...
# ***   *****   *******
# .*.   ..*..   ...*...
#       ..*..   ...*...
#               ...*...
# 크기가 N×M이고, '.'과 '*'로 이루어진 격자판이 주어진다. 이때, 십자가만을 이용해서 격자판과 같은 모양을 만들 수 있는지 구해보자. 십자가는 서로 겹쳐도 된다. 사용할 수 있는 십자가의 개수는 N×M이하이어야 한다. 격자판의 행은 위에서부터 1번, 열은 왼쪽에서부터 1번으로 번호가 매겨져 있다.


import sys

N,M = map(int,sys.stdin.readline().split())

graph = []
check = []
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    ch = []
    for j in temp:
        if j == '.':
            ch.append(0)
        else:
            ch.append(1)
    check.append(ch)
    graph.append(temp)



ix = [-1,0,1,0]
iy = [0,-1,0,1]
ans = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == '*':
            cnt = 0
            cross = []
            size = 0
            while True:
                size += 1
                for k in range(4):
                    dx = i+ix[k]*size
                    dy = j+iy[k]*size
                    if dx<0 or dy<0 or dx>=N or dy>=M:
                        cnt = -1
                        break
                    if graph[dx][dy] != '*':
                        cnt = -1
                        break
                    cross.append((dx,dy))
                if cnt == -1:
                    break
                cross.append((i,j))
                cnt += 1
                for x,y in cross:
                    check[x][y] = 0
                ans.append((i+1,j+1,cnt))

for i in check:
    if sum(i) != 0:
        ans = -1
        break

if ans == -1:
    print(ans)
else:
    print(len(ans))
    for i in ans:
        print(*i)