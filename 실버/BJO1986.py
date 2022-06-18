# n×m 크기의 체스 판과, 상대팀의 Queen, Knight, Pawn의 위치가 주어져 있을 때, 안전한 칸이 몇 칸인지 세는 프로그램을 작성하시오. (안전한 칸이란 말은 그 곳에 자신의 말이 있어도 잡힐 가능성이 없다는 것이다.)

# 참고로 Queen은 가로, 세로, 대각선으로 갈 수 있는 만큼 최대한 많이 이동을 할 수 있는데 만약 그 중간에 장애물이 있다면 이동을 할 수 없다. 그리고 Knight는 2×3 직사각형을 그렸을 때, 반대쪽 꼭짓점으로 이동을 할 수 있다. 아래 그림과 같은 8칸이 이에 해당한다.



# 이때 Knight는 중간에 장애물이 있더라도 이동을 할 수 있다. 그리고 Pawn은 상대팀의 말은 잡을 수 없다고 하자(즉, 장애물의 역할만 한다는 것이다).

# 예를 들어 다음과 같이 말이 배치가 되어 있다면 진하게 표시된 부분이 안전한 칸이 될 것이다. (K : Knight, Q : Queen, P : Pawn)

import sys

N,M = map(int,sys.stdin.readline().split())

temp = list(map(int,sys.stdin.readline().split()))
queen = []
for i in range(1,len(temp),2):
    queen.append((temp[i]-1,temp[i+1]-1))

temp = list(map(int,sys.stdin.readline().split()))
knight = []
for i in range(1,len(temp),2):
    knight.append((temp[i]-1,temp[i+1]-1))


temp = list(map(int,sys.stdin.readline().split()))
pawn = []
for i in range(1,len(temp),2):
    pawn.append((temp[i]-1,temp[i+1]-1))



check = [[0 for _ in range(M)] for _ in range(N)]

for x,y in queen:
    check[x][y] = 'Q'
for x,y in knight:
    check[x][y] = 'K'
for x,y in pawn:
    check[x][y] = 'P'
    

for x,y in queen:
    tx = x-1
    while tx >= 0 and check[tx][y] in (0,1):
        check[tx][y] = 1
        tx -= 1
    tx = x+1
    while tx < N and check[tx][y] in (0,1):
        check[tx][y] = 1
        tx += 1
    
    ty = y-1
    while ty >= 0 and check[x][ty] in (0,1):
        check[x][ty] = 1
        ty -= 1

    ty = y+1
    while ty < M and check[x][ty] in (0,1):
        check[x][ty] = 1
        ty += 1

    tx = x-1
    ty = y-1
    while tx >= 0 and ty >= 0 and check[tx][ty] in (0,1):
        check[tx][ty] = 1
        tx -= 1
        ty -= 1
    
    tx = x+1
    ty = y-1
    while tx < N and ty >= 0 and check[tx][ty] in (0,1):
        check[tx][ty] = 1
        tx += 1
        ty -= 1
    
    tx = x-1
    ty = y+1
    while tx >= 0 and ty < M and check[tx][ty] in (0,1):
        check[tx][ty] = 1
        tx -= 1
        ty += 1
    
    tx = x+1
    ty = y+1
    while tx < N and ty < M and check[tx][ty] in (0,1):
        check[tx][ty] = 1
        tx += 1
        ty += 1
    

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

for x,y in knight:
    for i in range(8):
        tx = x+dx[i]
        ty = y+dy[i]

        if tx < 0 or tx >= N or ty < 0 or ty >= M:
            continue
        if check[tx][ty] != 0:
            continue
        check[tx][ty] = 1

ans = 0
for i in range(N):
    for j in range(M):
        if check[i][j] == 0:
            ans += 1
print(ans)