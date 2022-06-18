# N개의 쿼리가 주어졌을 때, 쿼리를 수행해보자. 쿼리는 총 2가지 종류가 있고 아래와 같다. 가장 처음에 집합에는 아무것도 없다.

# 1 x y (x < y): 새로운 구간 (x, y)를 집합에 추가한다. 구간의 크기는 이전에 추가된 구간의 크기보다 크다.
# 2 a b (a ≠ b): a번째 추가된 구간에서 b번째 추가된 구간으로 이동하는 경로가 있으면 1, 없으면 0을 출력한다. 가장 처음 추가된 구간은 1번째 구간이다.
# 구간 (x1, y1)에서 구간 (x2, y2)로 이동하려면 x2 < x1 < y2 또는 x2 < y1 < y2를 만족해야 한다. 구간 I1에서 I2로 이동하는 경로가 있다는 것은 I1에서 I2로 집합에 추가된 구간만을 이용해서 이동할 수 있을 때이다.


import sys
from collections import deque

n = int(sys.stdin.readline())

query = []
for i in range(n):
    que,x,y = map(int,sys.stdin.readline().split())
    if que == 1:
        query.append((x,y))
    else:
        ax,ay = query[x-1]
        bx,by = query[y-1]
        check = [0]*len(query)
        check[x-1] = 1
        check[y-1] = 1
        qu = deque()
        qu.append((ax,ay))
        ans = 0
        while qu:
            tx,ty = qu.popleft()
            if (tx < by and tx > bx) or (ty < by and ty > bx):
                ans = 1
                break
            for j in range(len(query)):
                if check[j] == 1:
                    continue
                if (tx > query[j][0] and tx < query[j][1]) or (query[j][0] < ty and ty < query[j][1]):
                    check[j] = 1
                    qu.append((query[j][0],query[j][1]))
        print(ans)