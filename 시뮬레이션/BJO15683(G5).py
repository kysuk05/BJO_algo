# 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 
# 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

# CCTV의 최대 개수는 8개를 넘지 않는다.

import sys
from collections import deque
from copy import deepcopy
n,m = map(int,sys.stdin.readline().split())
graph = []
queue = deque()
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

anlis = []
def check(graph):
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                ans += 1
    if not anlis or anlis[-1] > ans:
        anlis.append(ans)
    return

def left(x,y,graph):
    nx = x
    ny = y
    while nx >= 0:
        if graph[nx][ny] == 6:
            break
        graph[nx][ny] = '1'
        nx -= 1
    return graph
def right(x,y,graph):
    nx = x
    ny = y
    while nx < n:
        if graph[nx][ny] == 6:
            break
        graph[nx][ny] = '1'
        nx += 1
    return graph
def up(x,y,graph):
    nx = x
    ny = y
    while ny < m:
        if graph[nx][ny] == 6:
            break
        graph[nx][ny] = '1'
        ny += 1
    return graph
def down(x,y,graph):
    nx = x
    ny = y
    while ny >= 0:
        if graph[nx][ny] == 6:
            break
        graph[nx][ny] = '1'
        ny -= 1
    return graph

def main(graph,queue):
    graph1 = graph
    if queue:
        queue1 = deepcopy(queue)
        a,x,y = queue1.popleft()
        if a == 1:
            for i in range(4):
                graph1 = deepcopy(graph)
                if i == 0:
                    graph1 = left(x,y,graph1)
                elif i == 1:
                    graph1 = right(x,y,graph1)
                elif i == 2:
                    graph1 = up(x,y,graph1)
                elif i == 3:
                    graph1 = down(x,y,graph1)
                main(graph1,queue1)
        elif a == 2:
            for i in range(2):
                graph1 = deepcopy(graph)
                if i == 0:
                    graph1 = left(x,y,graph1)
                    graph1 = right(x,y,graph1)
                elif i == 1:
                    graph1 = up(x,y,graph1)
                    graph1 = down(x,y,graph1)
                main(graph1,queue1)
        elif a == 3:
            for i in range(4):
                graph1 = deepcopy(graph)
                if i == 0:
                    graph1 = left(x,y,graph1)
                    graph1 = up(x,y,graph1)
                elif i == 1:
                    graph1 = left(x,y,graph1)
                    graph1 = down(x,y,graph1)
                elif i == 2:
                    graph1 = right(x,y,graph1)
                    graph1 = up(x,y,graph1)
                elif i == 3:
                    graph1 = right(x,y,graph1)
                    graph1 = down(x,y,graph1)
                main(graph1,queue1)
            
        elif a == 4:
            for i in range(4):
                graph1 = deepcopy(graph)
                if i == 0:
                    graph1 = left(x,y,graph1)
                    graph1 = right(x,y,graph1)
                    graph1 = up(x,y,graph1)
                elif i == 1:
                    graph1 = left(x,y,graph1)
                    graph1 = right(x,y,graph1)
                    graph1 = down(x,y,graph1)
                elif i == 2:
                    graph1 = left(x,y,graph1)
                    graph1 = up(x,y,graph1)
                    graph1 = down(x,y,graph1)
                elif i == 3:
                    graph1 = right(x,y,graph1)
                    graph1 = up(x,y,graph1)
                    graph1 = down(x,y,graph1)
                main(graph1,queue1)
        elif a == 5:
            graph1 = deepcopy(graph)
            graph1 = left(x,y,graph1)
            graph1 = right(x,y,graph1)
            graph1 = up(x,y,graph1)
            graph1 = down(x,y,graph1)
            main(graph1,queue1)
    
    else:
        check(graph1)






for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6 :
            queue.append((graph[i][j],i,j))

main(graph,queue)
print(anlis[-1])