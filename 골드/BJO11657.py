# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.


import sys

inf = sys.maxsize
N,M = map(int,sys.stdin.readline().split())


graph = [[]for i in range(N+1)]
dist = [inf]*(N+1)

for i in range(M):
    st,en,dis = map(int,sys.stdin.readline().split())
    graph[st].append((en,dis))

dist[1] = 0


min_gra = 0

for i in range(M):
    for j in range(1,N+1):
        if dist[j] == inf:
            continue
        for en,dis in graph[j]:
            if dist[en] > dist[j] + dis:
                dist[en] = dist[j] + dis
                if i == M-1:
                    min_gra = 1

if min_gra == 1:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])