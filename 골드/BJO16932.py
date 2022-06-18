# N×M인 배열에서 모양을 찾으려고 한다. 배열의 각 칸에는 0과 1 중의 하나가 들어있다. 두 칸이 서로 변을 공유할때, 두 칸을 인접하다고 한다.

# 1이 들어 있는 인접한 칸끼리 연결했을 때, 각각의 연결 요소를 모양이라고 부르자. 모양의 크기는 모양에 포함되어 있는 1의 개수이다.

# 배열의 칸 하나에 들어있는 수를 변경해서 만들 수 있는 모양의 최대 크기를 구해보자.


import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())


graph = []

for i in range(N):
    temp = list(sys.stdin.readline().split())
    graph.append(temp)

zero_arr = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            zero_arr.append((i,j))



dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
qu = deque()

check = [[0 for i in range(M)]for j in range(N)]
cnt = 1


for i in range(N):
    for j in range(M):
        if graph[i][j] == '1' and check[i][j] == 0:
            shape_li = []
            shape_li.append((i,j))
            size = 1
            qu.append((i,j))
            check[i][j] = 1
            
            while qu:
                x,y = qu.popleft()
                for t in range(4):
                    ix = x+dx[t]
                    iy = y+dy[t]
                    if ix < 0 or ix >= N or iy < 0 or iy >= M:
                        continue
                    if check[ix][iy] != 0:
                        continue
                    if graph[ix][iy] != '1':
                        continue
                    qu.append((ix,iy))
                    shape_li.append((ix,iy))
                    check[ix][iy] = 1
                    size += 1
            while shape_li:
                x,y = shape_li.pop()
                graph[x][y] = (cnt,size)
            ans = max(ans,size)
            cnt += 1
ans += 1

for x,y in zero_arr:
    temp = []
    t_ans = 0
    for i in range(4):
        ix = x+dx[i]
        iy = y+dy[i]
        if ix < 0 or ix >= N or iy < 0 or iy >= M:
            continue
        if graph[ix][iy] == '0':
            continue
        if graph[ix][iy] not in temp:
            temp.append(graph[ix][iy])
    if len(temp) >= 2:
        for i in range(len(temp)):
            t_ans += temp[i][1]
    ans = max(ans,t_ans+1)
    
print(ans)