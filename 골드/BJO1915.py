# n×m의 0, 1로 된 배열이 있다. 이 배열에서 1로 된 가장 큰 정사각형의 크기를 구하는 프로그램을 작성하시오.

# 0	1	0	0
# 0	1	1	1
# 1	1	1	0
# 0	0	1	0
# 위와 같은 예제에서는 가운데의 2×2 배열이 가장 큰 정사각형이다. 

import sys

n,m = map(int,sys.stdin.readline().split())

li = []

for i in range(n):
    t = sys.stdin.readline().rstrip()
    lis = []
    for j in t:
        lis.append(j)
    li.append(lis)

graph = [[0 for i in range(m)]for j in range(n)]

t = 0
for i in range(m):
    for j in range(n):
        if li[j][i] == '1':
            if i-1 >= 0 and j-1 >= 0:
                graph[j][i] = (int(min(graph[j-1][i],graph[j][i-1],graph[j-1][i-1])**0.5)+1)**2
                if graph[j][i] > t:
                    t = graph[j][i]
            else:
                graph[j][i] = 1
                if graph[j][i] > t:
                    t = graph[j][i]

print(t)