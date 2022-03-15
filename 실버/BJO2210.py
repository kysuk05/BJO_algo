# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
# 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

import sys


graph = []
for i in range(5):
    li = list(sys.stdin.readline().split())
    graph.append(li)

dic = {}

dx = [-1,0,1,0]
dy = [0,-1,0,1]

ans = 0
def check(x,y,n,num):
    global ans
    if n == 6:
        if num not in dic:
            dic[num] = 0
            ans += 1
        return
    else:
        for i in range(4):
            ix = x+dx[i]
            iy = y+dy[i]
            if ix <0 or ix>=5 or iy<0 or iy>=5:
                continue
            else:
                num += graph[ix][iy]
                check(ix,iy,n+1,num)
                num = num[:-1]


for i in range(len(graph)):
    for j in range(len(graph[i])):
        check(i,j,1,graph[i][j])

print(ans)