# 총 25명의 여학생들로 이루어진 여학생반은 5×5의 정사각형 격자 형태로 자리가 배치되었고, 얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다. 
# 곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.

# 위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. 
# ‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.

# 이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
# 강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
# 화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
# 그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.
# 여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.




import sys
from collections import deque


lis = []
queue = deque()
for i in range(5):
    li = []
    k = sys.stdin.readline().rstrip()
    for j in k:
        li.append(j)
    lis.append(li)


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def func(x,y,k,yeon,som):
    global ans
    if k == 7:
        if som >= 4:
            ans +=1
        return
    else:
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if check[nx][ny] != 0:
                    continue
                if lis[nx][ny] == 'Y':
                    if yeon > 3:
                        continue
                    else:
                        yeon += 1
                        check[nx][ny] = 1
                        queue.append((nx,ny))
                        k += 1
                if lis[nx][ny] == 'S':
                    check[nx][ny] = 1
                    som += 1
                    queue.append((nx,ny))
                    k += 1
            
                func(nx,ny,k,yeon,som)

ans = 0

for i in range(5):
    for j in range(5):
        if lis[i][j] == 'S':
            queue.append((i,j))
            check = [[0 for a in range(5)] for b in range(5)]
            func(i,j,0,0,0)
print(ans)