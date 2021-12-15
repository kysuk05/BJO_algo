# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.


import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().split())

graph = [[0]for _ in range(n+1)]
for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    if graph[x] == [0]:
        graph[x] = [y]
    else:
        graph[x].append(y)
    if graph[y] == [0]:
        graph[y] = [x]
    else:
        graph[y].append(x)

for i in graph:
    i.sort()
check1 = [0]*(n+1)
check2 = [0]*(n+1)
check1[v] = 1
check2[v] = 1
stack = [v]
qu = deque()
qu.append(v)
ans1 = [v]
ans2 = [v]
def dfs():
    while stack:
        x = stack.pop()
        for i in graph[x]:
            if graph[i] != [0] and check1[i] == 0:
                check1[i] = 1
                ans1.append(i)
                stack.append(i)
            dfs()

def bfs():
    while qu:
        x = qu.popleft()
        for i in graph[x]:
            if graph[i] != [0] and check2[i] == 0:
                check2[i] = 1
                ans2.append(i)
                qu.append(i)
dfs()
bfs()
for i in (ans1):
    print(i,end=' ')
print()
for j in (ans2):
    print(j,end=' ')