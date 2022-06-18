# 종우는 18학번을 대표하여 중앙대학교 개교 100주년 기념 퍼레이드의 경로 선정 위원으로 선정되었다. 퍼레이드의 경로는 일정한 지점들과 두 지점을 연결하는 연결 구간으로 이루어져 있다. 종우는 모든 지점을 지나면서 모든 연결 구간들을 지나고 싶어한다.

# 하지만 같은 연결 구간을 두 번 이상 지날 경우 그 구간의 주민들이 민원을 제기하게 된다. 단, 같은 지점은 두 번 이상 지나도 된다.

# 민원을 받지 않으면서 모든 구간을 지나도록 퍼레이드를 만들고 싶은 종우를 위한 프로그램을 작성해보도록 하자.

import sys
from collections import deque

V,E = map(int,sys.stdin.readline().split())
graph = [[]for i in range(V+1)]

for i in range(E):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0 for i in range(V+1)]

qu = deque()
qu.append(1)
check[1] = 1

while qu:
    x = qu.popleft()
    for i in graph[x]:
        if check[i] == 0:
            check[i] = 1
            qu.append(i)

if sum(check) != V:
    print('NO')
else:
    ans = 0
    for i in range(1,V):
        if len(graph[i]) % 2 == 1:
            ans += 1
    
    if ans <= 2:
        print('YES')
    else:
        print('NO')