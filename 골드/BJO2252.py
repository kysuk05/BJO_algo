# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.


import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[]for i in range(N+1)]
check = [0 for i in range(N+1)]

qu = deque()

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    
    graph[x].append(y)
    check[y] += 1


ans = []

for i in range(1,N+1):
    if check[i] == 0:
        qu.append(i)

while qu:
    x = qu.popleft()
    ans.append(x)
    for i in graph[x]:
        check[i] -= 1
        if check[i] == 0:
            qu.append(i)
print(*ans)