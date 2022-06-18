# 문제
# 홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다. 미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나, 벽을 포함하고 있다. 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 홍준이는 미로에서 모든 행과 열의 이동할 수 있는 칸을 걸어다녔다. 그러면서 자신의 움직임을 모두 노트에 쓰기로 했다. 홍준이는 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.

# 입력으로 홍준이가 적은 내용을 나타내는 문자열이 주어진다. 각 문자 하나는 한 번의 움직임을 말한다. ‘F’는 앞으로 한 칸 움직인 것이고, ‘L'과 ’R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다. 즉, 90도를 회전하면서, 위치는 그대로인 것이다.

dx = [0,1,0,-1]
dy = [1,0,-1,0]


check = [[0 for _ in range(102)]for _ in range(102)]

loc = [50,50]

direct = 0

N = int(input())
way = input()

check[loc[0]][loc[1]] = 1

for i in range(N):
    temp = way[i]
    if temp == 'R':
        direct += 1
        direct %= 4
    elif temp == 'L':
        direct -= 1
        direct %= 4
    else:
        loc[0] += dx[direct]
        loc[1] += dy[direct]

        check[loc[1]][loc[0]] = 1

x_loc = set()
y_loc = set()

for i in range(102):
    for j in range(102):
        if check[i][j] == 1:
            x_loc.add(j)
            y_loc.add(i)


x_loc = sorted(list(x_loc))
y_loc = sorted(list(y_loc))

ans = []

for i in range(y_loc[0],y_loc[-1]+1):
    temp = []
    for j in range(x_loc[0],x_loc[-1]+1):
        if check[i][j] == 1:
            temp.append('.')
        else:
            temp.append('#')
    ans.append(temp)


for i in range(len(ans)):
    for j in range(len(ans[i])-1,-1,-1):
        print(ans[i][j],end='')
    print()