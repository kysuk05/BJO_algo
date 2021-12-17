# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

# 빈 칸의 개수는 3개 이상이다.

# 출력
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

# python 시간초과
# import sys
# from collections import deque

# n,m = map(int,sys.stdin.readline().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int,sys.stdin.readline().split())))


# empty = []
# vi = []
# for y in range(m):
#     for x in range(n):
#         wal = m*n
#         if graph[x][y] == 0:
#             empty.append((x,y))
#             wal -= 1
#         elif graph[x][y] == 2:
#             vi.append((x,y))
#             wal -= 1



# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# ans = 0
# def bfs(map,sp):
#     global ans
#     an = 0
#     while sp:
#         x,y = sp.pop()
#         for t in range(4):
#             nx = x+dx[t]
#             ny = y+dy[t]
#             if nx < 0 or nx >= n or ny < 0 or ny>=m:
#                 continue
#             if map[nx][ny] == 0:
#                 map[nx][ny] = 2
#                 sp.append((nx,ny))
#     for i in range(m):
#         for j in range(n):
#             if map[j][i] == 0:
#                 an +=1
#     ans = max(an,ans)
    
# new = []
# def wall(cnt):
#     if cnt == 3:
#         gra = [t[:] for t in graph]
#         sp = [v[:] for v in vi]
#         bfs(gra,sp)
#     if cnt < 3:
#         for a in range(m):
#             for b in range(n):
#                 if graph[a][b] == 0:
#                     graph[a][b] = 1
#                     cnt += 1
#                     wall(cnt)
#                     cnt -= 1
#                     graph[a][b] = 0


# wall(0)
# print(ans)

#
from copy import deepcopy
import sys
from itertools import combinations
from collections import deque




n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


empty = []
vi = []
for y in range(m):
    for x in range(n):
        if graph[x][y] == 0:
            empty.append((x,y))
        elif graph[x][y] == 2:
            vi.append((x,y))

nw = list(combinations(empty,3))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
def bfs(gr,vir):
    global ans
    an = 0
    while vir:
        x,y = vir.pop()
        for t in range(4):
            nx = x+dx[t]
            ny = y+dy[t]
            if nx < 0 or nx >= n or ny < 0 or ny>=m:
                continue
            if gr[nx][ny] == 0:
                gr[nx][ny] = 2
                vir.append((nx,ny))
    for i in range(m):
        for j in range(n):
            if gr[j][i] == 0:
                an +=1
    ans = max(an,ans)
    
while nw:
    gra = deepcopy(graph)
    k = nw.pop()
    for x,y in k:
        gra[x][y] = 1
    vir = deepcopy(vi)
    bfs(gra,vir)
print(ans)