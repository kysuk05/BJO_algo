# 첫째 줄에 노트북의 세로와 가로 길이를 나타내는 N(1 ≤ N ≤ 40)과 M(1 ≤ M ≤ 40), 
# 그리고 스티커의 개수 K(1 ≤ K ≤ 100)이 한 칸의 빈칸을 사이에 두고 주어진다.

# 그 다음 줄부터는 K개의 스티커들에 대한 정보가 주어진다. 
# 각 스티커는 아래와 같은 형식으로 주어진다.

# 먼저 i번째 스티커가 인쇄된 모눈종이의 행의 개수와 열의 개수를 나타내는 Ri(1 ≤ Ri ≤ 10)와 Ci(1 ≤ Ci ≤ 10)가 한 칸의 빈칸을 사이에 두고 주어진다.

# 다음 Ri개의 줄에는 각 줄마다 모눈종이의 각 행을 나타내는 Ci개의 정수가 한 개의 빈칸을 사이에 두고 주어진다. 
# 각 칸에 들어가는 값은 0, 1이다. 0은 스티커가 붙지 않은 칸을, 1은 스티커가 붙은 칸을 의미한다.

# 문제에서 설명한 것과 같이 스티커는 모두 올바른 모눈종이에 인쇄되어 있다. 
# 구체적으로 스티커의 각 칸은 상하좌우로 모두 연결되어 있고, 
# 모눈종이의 크기는 스티커의 크기에 꼭 맞아서 상하좌우에 스티커에 전혀 포함되지 않는 불필요한 행이나 열이 존재하지 않는다.

import sys
from collections import deque
n,m,k = map(int,sys.stdin.readline().split())

queue = deque()


for i in range(k):
    li = []
    x,y = map(int,sys.stdin.readline().split())
    for j in range(x):
        li.append(list(map(int,sys.stdin.readline().split())))
    queue.append((x,y,li))


graph = [[0 for a in range(m)]for b in range(n)]



    

def che(x,y,qu,graph,check):
    for i in range(n):
        for j in range(m):
            if i+x-1 >= n or j+y-1 >= m:
                continue
            ch = []
            check = 0
            for a in range(x):
                for b in range(y):
                    if qu[a][b] == 1:
                        if graph[i+a][j+b] == 0:
                            ch.append((i+a,j+b))
                        else:
                            check = 1
                            break
                    if a == x-1 and b == y-1 and check == 0:
                        while ch:
                            n1,n2 = ch.pop()
                            graph[n1][n2] = 1
                        return x,y,qu,graph,check
                if check == 1:
                    break

                
def mv(x,y,qu):
    qu1 = [[0 for a in range(x)] for b in range(y)]
    for i in range(x):
        for j in range(y):
            if qu[i][j] == 1:
                qu1[j][x-i-1] = 1
    
    return y,x,qu1
                

while queue:
    x,y,qu = queue.popleft()
    check = 0
    for move in range(4):
        k = che(x,y,qu,graph,check)
        if k:
            x,y,qu,graph,check = k
            break
        x,y,qu = mv(x,y,qu)

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans +=1

print(ans)

