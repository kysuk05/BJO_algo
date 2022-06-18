# 크기가 N×M 크기인 배열 A가 있을때, 배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다. 배열 A가 아래와 같은 경우 1행의 합은 6, 2행의 합은 4, 3행의 합은 15이다. 따라서, 배열 A의 값은 4이다.

# 1 2 3
# 2 1 1
# 4 5 6
# 배열은 회전 연산을 수행할 수 있다. 회전 연산은 세 정수 (r, c, s)로 이루어져 있고, 가장 왼쪽 윗 칸이 (r-s, c-s), 가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형을 시계 방향으로 한 칸씩 돌린다는 의미이다. 배열의 칸 (r, c)는 r행 c열을 의미한다.

# 예를 들어, 배열 A의 크기가 6×6이고, 회전 연산이 (3, 4, 2)인 경우에는 아래 그림과 같이 회전하게 된다.

# A[1][1]   A[1][2] → A[1][3] → A[1][4] → A[1][5] → A[1][6]
#              ↑                                       ↓
# A[2][1]   A[2][2]   A[2][3] → A[2][4] → A[2][5]   A[2][6]
#              ↑         ↑                   ↓         ↓
# A[3][1]   A[3][2]   A[3][3]   A[3][4]   A[3][5]   A[3][6]
#              ↑         ↑                   ↓         ↓
# A[4][1]   A[4][2]   A[4][3] ← A[4][4] ← A[4][5]   A[4][6]
#              ↑                                       ↓
# A[5][1]   A[5][2] ← A[5][3] ← A[5][4] ← A[5][5] ← A[5][6]

# A[6][1]   A[6][2]   A[6][3]   A[6][4]   A[6][5]   A[6][6]
# 회전 연산이 두 개 이상이면, 연산을 수행한 순서에 따라 최종 배열이 다르다.

# 다음은 배열 A의 크기가 5×6이고, 회전 연산이 (3, 4, 2), (4, 2, 1)인 경우의 예시이다.

# 1 2 3 2 5 6
# 3 8 7 2 1 3
# 8 2 3 1 4 5
# 3 4 5 1 1 1
# 9 3 2 1 4 3
# 1 8 2 3 2 5
# 3 2 3 7 2 6
# 8 4 5 1 1 3
# 3 3 1 1 4 5
# 9 2 1 4 3 1
# 1 8 2 3 2 5
# 3 2 3 7 2 6
# 3 8 4 1 1 3
# 9 3 5 1 4 5
# 2 1 1 4 3 1
# 배열 A	(3, 4, 2) 연산 수행 후	(4, 2, 1) 연산 수행 후
# 1 2 3 2 5 6
# 3 8 7 2 1 3
# 8 2 3 1 4 5
# 3 4 5 1 1 1
# 9 3 2 1 4 3
# 1 2 3 2 5 6
# 3 8 7 2 1 3
# 3 8 2 1 4 5
# 9 4 3 1 1 1
# 3 2 5 1 4 3
# 1 8 2 3 2 5
# 3 8 2 7 2 6
# 3 4 3 1 1 3
# 9 2 1 1 4 5
# 3 5 1 4 3 1
# 배열 A	(4, 2, 1) 연산 수행 후	(3, 4, 2) 연산 수행 후
# 배열 A에 (3, 4, 2), (4, 2, 1) 순서로 연산을 수행하면 배열 A의 값은 12, (4, 2, 1), (3, 4, 2) 순서로 연산을 수행하면 15 이다.

# 배열 A와 사용 가능한 회전 연산이 주어졌을 때, 배열 A의 값의 최솟값을 구해보자. 회전 연산은 모두 한 번씩 사용해야 하며, 순서는 임의로 정해도 된다.

import sys
from itertools import permutations
from collections import deque

N,M,K = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

order = []
for _ in range(K):
    r,c,s = map(int,sys.stdin.readline().split())
    order.append((r,c,s))

order = permutations(order,K)


def move(temp_list, change_order):
    for i in range(1,change_order[2]+1):
        st_x = change_order[1] - i -1
        st_y = change_order[0] - i -1
        en_x = change_order[1] + i -1
        en_y = change_order[0] + i -1
        location = []
        loc_num = deque()
        
        for x in range(st_x,en_x):
            location.append((st_y,x))
            loc_num.append(temp_list[st_y][x])
        for y in range(st_y,en_y):
            location.append((y,en_x))
            loc_num.append(temp_list[y][en_x])
        for x in range(en_x,st_x-1,-1):
            location.append((en_y,x))
            loc_num.append(temp_list[en_y][x])
        for y in range(en_y-1,st_y-1,-1):
            location.append((y,st_x))
            loc_num.append(temp_list[y][st_x])
        
        
        temp = loc_num.pop()
        loc_num.appendleft(temp)
        cnt = 0
        for y,x in location:
            temp_list[y][x] = loc_num[cnt]
            cnt+=1
    
    return temp_list


ans = sys.maxsize

for change in order:
    temp = [item[:] for item in graph]
    for i in change:
        temp = move(temp,i)

    for j in range(N):
        ans = min(ans,sum(temp[j]))

print(ans)