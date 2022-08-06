# 아주 먼 미래에 사람들이 가장 많이 사용하는 대중교통은 하이퍼튜브이다. 하이퍼튜브 하나는 역 K개를 서로 연결한다. 
# 1번역에서 N번역으로 가는데 방문하는 최소 역의 수는 몇 개일까?


from collections import deque

import sys

N,K,M = map(int,sys.stdin.readline().split())

qu = deque()

graph = [{}for _ in range(N+M+1)]

for i in range(M):
    station = list(map(int,sys.stdin.readline().split()))
    for j in station:
        graph[j][N+i+1] = 0
        graph[N+i+1][j] = 0

check = [0]*(N+M+1)

check[1] = 1
qu.append(1)

while qu:
    x = qu.popleft()
    for i in graph[x]:
        if check[i] != 0:
            continue
        qu.append(i)
        if i > N:
            check[i] = check[x]
        else:
            check[i] = check[x]+1


if check[N] == 0:
    print(-1)
else:
    print(check[N])