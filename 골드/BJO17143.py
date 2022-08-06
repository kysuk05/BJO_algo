# 낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다. 격자판의 각 칸은 (r, c)로 나타낼 수 있다. r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다. 칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.



# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다. 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.

# 왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다. 상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력이다. 왼쪽 위에 상어를 구분하기 위해 문자를 적었다.



# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.

import sys

R,C,M = map(int,sys.stdin.readline().split())

shark = {}

for i in range(M):
    r,c,s,d,z = map(int,sys.stdin.readline().split())
    shark[r,c] = [s,d,z]


ans = 0
for i in range(1,C+1):
    temp = []
    for j in shark.keys():
        if j[1] == i:
            temp.append(j)
    temp.sort()
    if temp:
        ans += shark[temp[0]][2]
        del shark[temp[0]]
    
    sh = {}
    for j in shark.keys():
        if shark[j][1] == 1:
            x = j[0]-shark[j][0]-1
            y = j[1]
            if (x//(R-1))%2 == 0:
                k = 1
            else:
                k = 2
            
            if k == 1:
                x = x%(R-1)+1
            else:
                x = R-(x%(R-1))

            if (x,y) in sh:
                if shark[j][2] > sh[(x,y)][2]:
                    sh[(x,y)] = [shark[j][0],k,shark[j][2]]
            else:
                sh[(x,y)] = [shark[j][0],k,shark[j][2]]
        
        
        elif shark[j][1] == 2:
            x = j[0]+shark[j][0]-1
            y = j[1]
            if (x//(R-1))%2 == 0:
                k = 2
            else:
                k = 1
            
            if k == 2:
                x = x%(R-1)+1
            else:
                x = R-(x%(R-1))
            
            if (x,y) in sh:
                if shark[j][2] > sh[(x,y)][2]:
                    sh[(x,y)] = [shark[j][0],k,shark[j][2]]
            else:
                sh[(x,y)] = [shark[j][0],k,shark[j][2]]
        
        
        elif shark[j][1] == 3:
            x = j[0]
            y = j[1]+shark[j][0]-1
            if (y//(C-1))%2 == 0:
                k = 3
            else:
                k = 4
            
            if k == 3:
                y = y%(C-1)+1
            else:
                y = C-(y%(C-1))
            
            if (x,y) in sh:
                if shark[j][2] > sh[(x,y)][2]:
                    sh[(x,y)] = [shark[j][0],k,shark[j][2]]
            else:
                sh[(x,y)] = [shark[j][0],k,shark[j][2]]
        
        
        elif shark[j][1] == 4:
            x = j[0]
            y = j[1]-shark[j][0]-1
            if (y//(C-1))%2 == 0:
                k = 4
            else:
                k = 3
            
            if k == 4:
                y = y%(C-1)+1
            else:
                y = C-(y%(C-1))
            
            
            if (x,y) in sh:
                if shark[j][2] > sh[(x,y)][2]:
                    sh[(x,y)] = [shark[j][0],k,shark[j][2]]
            else:
                sh[(x,y)] = [shark[j][0],k,shark[j][2]]
    shark = sh

print(ans)