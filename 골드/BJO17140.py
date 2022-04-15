# 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.

# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

# 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.

# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.

# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.

# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.


import sys
from collections import Counter

r,c,k = map(int,sys.stdin.readline().split())

graph = []

for i in range(3):
    graph.append(list(map(int,sys.stdin.readline().split())))


def R(graph):
    max_len = 0
    for i in range(len(graph)):
        graph[i].sort(reverse=True)
        while graph[i][-1] == 0:
            graph[i].pop()
        temp = list(Counter(graph[i]).items())
        temp.sort()
        temp.sort(key = lambda x: x[1])
        graph[i] = []
        for a,b in temp:
            graph[i].append(a)
            graph[i].append(b)
        max_len = max(max_len,len(graph[i]))
    
    for i in range(len(graph)):
        while len(graph[i]) != max_len:
            graph[i].append(0)
    return graph

def D(graph):
    for i in range(len(graph)):
        graph.append([0 for _ in range(len(graph[0]))])
    
    for i in range(len(graph[0])):
        temp = []
        for j in range(len(graph)):
            if graph[j][i] != 0:
                temp.append(graph[j][i])
        temp = list(Counter(temp).items())
        temp.sort()
        temp.sort(key = lambda x: x[1])
        
        n_graph = []
        for a,b in temp:
            n_graph.append(a)
            n_graph.append(b)
        while len(n_graph) != len(graph):
            n_graph.append(0)
        for j in range(len(graph)):
            graph[j][i] = n_graph[j]
    
    while sum(graph[-1]) == 0:
        graph.pop()
    return graph

ans = -1
for _ in range(101):
    if len(graph) >= r and len(graph[0]) >= c and graph[r-1][c-1] == k:
        ans = _
        break
    
    if len(graph) >= len(graph[0]):
        graph = R(graph)
    else:
        graph = D(graph)

print(ans)