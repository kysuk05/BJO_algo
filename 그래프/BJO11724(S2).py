# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.


import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[]for i in range(n+1)]
for j in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

qu = deque()
check = [0]*(n+1)
ans = 0
def bfs():
    global ans
    while qu:
        x = qu.popleft()
        for i in graph[x]:
            if check[i] == 0:
                check[i] = 1
                qu.append(i)
    ans += 1

for i in range(len(check)):
    if check[i] == 0:
        check[i] = 1
        qu.append(i)
        bfs()

print(ans-1)