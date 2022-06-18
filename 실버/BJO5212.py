# 푸르고 아름다운 남해에는 많은 섬이 장관을 이루고 있다. 그림이 아니면 볼 수 없을 것 같은 아름다운 장관을 실제로 볼 수 있는 다도해로 상근이는 여행을 떠났다.

# 다도해에 도착한 상근이는 서울에서 보던 것과는 다른 풍경에 큰 충격을 받았다. 지구 온난화로 인해 해수면이 상승해 섬의 일부가 바다에 잠겨버렸다.

# 서울로 다시 돌아온 상근이는 이렇게 지구 온난화가 계속 될 경우 남해의 지도는 어떻게 바뀔지 궁금해졌다.

# 다도해의 지도는 R*C 크기의 그리드로 나타낼 수 있다. 'X'는 땅을 나타내고, '.'는 바다를 나타낸다.

# 50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다는 사실을 알았다.

# 상근이는 50년 후 지도를 그려보기로 했다. 섬의 개수가 오늘날보다 적어질 것이기 때문에, 지도의 크기도 작아져야 한다. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다. 50년이 지난 후에도 섬은 적어도 한 개 있다. 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.


import sys

R,C = map(int,sys.stdin.readline().split())

maps = []
for i in range(R):
    maps.append(list(sys.stdin.readline().rstrip()))


ix = [-1,0,1,0]
iy = [0,-1,0,1]

sink = []

for i in range(R):
    for j in range(C):
        if maps[i][j] != 'X':
            continue
        cnt = 0
        for t in range(4):
            dx = i+ix[t]
            dy = j+iy[t]
            if dx < 0 or dy < 0 or dx >= R or dy >= C:
                cnt += 1
                continue
            if maps[dx][dy] == '.':
                cnt += 1
        if cnt >= 3:
            sink.append((i,j))

for x,y in sink:
    maps[x][y] = '.'

min_x = (11,0)
max_x = (-1,0)
min_y = (0,11)
max_y = (0,-1)


for i in range(R):
    for j in range(C):
        if maps[i][j] != 'X':
            continue
        if i < min_x[0]:
            min_x = (i,j)
        if i > max_x[0]:
            max_x = (i,j)
        if j < min_y[1]:
            min_y = (i,j)
        if j > max_y[1]:
            max_y = (i,j)    


for i in range(min_x[0],max_x[0]+1):
    for j in range(min_y[1],max_y[1]+1):
        print(maps[i][j],end='')
    print()