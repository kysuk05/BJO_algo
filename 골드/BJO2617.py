# 모양은 같으나, 무게가 모두 다른 N개의 구슬이 있다. N은 홀수이며, 구슬에는 번호가 1,2,...,N으로 붙어 있다. 이 구슬 중에서 무게가 전체의 중간인 (무게 순서로 (N+1)/2번째) 구슬을 찾기 위해서 아래와 같은 일을 하려 한다.

# 우리에게 주어진 것은 양팔 저울이다. 한 쌍의 구슬을 골라서 양팔 저울의 양쪽에 하나씩 올려 보면 어느 쪽이 무거운가를 알 수 있다. 이렇게 M개의 쌍을 골라서 각각 양팔 저울에 올려서 어느 것이 무거운가를 모두 알아냈다. 이 결과를 이용하여 무게가 중간이 될 가능성이 전혀 없는 구슬들은 먼저 제외한다.

# 예를 들어, N=5이고, M=4 쌍의 구슬에 대해서 어느 쪽이 무거운가를 알아낸 결과가 아래에 있다.

# 구슬 2번이 구슬 1번보다 무겁다.
# 구슬 4번이 구슬 3번보다 무겁다.
# 구슬 5번이 구슬 1번보다 무겁다.
# 구슬 4번이 구슬 2번보다 무겁다.
# 위와 같이 네 개의 결과만을 알고 있으면, 무게가 중간인 구슬을 정확하게 찾을 수는 없지만, 1번 구슬과 4번 구슬은 무게가 중간인 구슬이 절대 될 수 없다는 것은 확실히 알 수 있다. 1번 구슬보다 무거운 것이 2, 4, 5번 구슬이고, 4번 보다 가벼운 것이 1, 2, 3번이다. 따라서 답은 2개이다.

# M 개의 쌍에 대한 결과를 보고 무게가 중간인 구슬이 될 수 없는 구슬의 개수를 구하는 프로그램을 작성하시오.



import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

beads = [[[],[]]for i in range(N+1)]
qu = deque()

for i in range(M):
    hev,lig = map(int,sys.stdin.readline().split())
    if lig not in beads[hev][0]:
        beads[hev][0].append(lig)
    if hev not in beads[lig][1]:
        beads[lig][1].append(hev)

ans = 0
for i in beads:
    for j in i[0]:
        qu.append(j)
    while qu:
        x = qu.popleft()
        for k in beads[x][0]:
            if k not in i[0]:
                i[0].append(k)
                qu.append(k)


    for j in i[1]:
        qu.append(j)
    while qu:
        x = qu.popleft()
        for k in beads[x][1]:
            if k not in i[1]:
                i[1].append(k)
                qu.append(k)
    if len(i[0]) > N//2 or len(i[1]) > N//2:
        ans += 1

print(ans)