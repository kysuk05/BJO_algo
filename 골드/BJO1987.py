# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

import sys

n,m = map(int,sys.stdin.readline().split())


graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
ch = 0
check = set()
for i in graph:
    for j in i:
        if j not in check:
            check.add(j)
            ch += 1

ix = [0,1,0,-1]
iy = [1,0,-1,0]




ans = 1

li = [0]*26
li[ord(graph[0][0])-65] = 1
stack = [(0,0)]



def back(stack,li,cn):
    global ans
    x = stack[-1][0]
    y = stack[-1][1]
    for i in range(4):
        dx = x+ix[i]
        dy = y+iy[i]
        if dx >= n or dy >= m or dx < 0 or dy < 0:
            continue
        temp = ord(graph[dx][dy])-65
        if li[temp] == 1:
            continue
        
        stack.append((dx,dy))
        li[temp] += 1
        ans = max(ans,cn+1)
        if ans == ch:
            print(ans)
            exit()
        back(stack,li,cn+1)
        stack.pop()
        li[temp] -= 1
        

back(stack,li,1)
print(ans)