# 생방송 플랫폼 Twitch에서 “Twitch Plays Pokémon”이라는 컨텐츠가 큰 유행을 끈 적이 있다. 이 방송은 시청자가 채팅으로 명령을 입력하면 그 명령이 게임에 반영되는 독특한 시스템을 사용해, 수십만 명이 합심해 하나의 게임을 진행한다는 특별한 경험을 제공했다. 막 데뷔한 스트리머 에리는 이 시스템을 빌려 “Twitch Plays VIIIbit Explorer” 컨텐츠를 진행하기로 했다.

# VIIIbit Explorer는 캐릭터를 조종해 던전을 탈출하는 간단한 게임이다. 던전은 격자로 나뉘어진 직사각형 모양이며, 몇몇 격자칸에는 아이템이 놓여 있다. 시청자는 다음과 같은 명령들을 입력해 캐릭터를 조종할 수 있다.

# U, D, L, R: 캐릭터를 위, 아래, 왼쪽, 오른쪽으로 한 칸 움직인다. 단, 던전 바깥으로 이동하게 되는 경우 던전을 둘러싸고 있는 용암에 빠져 게임 오버된다.
# P: 캐릭터가 위치한 칸에 놓여 있는 아이템을 줍는다. 단, 아이템이 없는 칸에서 이 명령을 사용하는 경우 바닥이 무너져 게임 오버된다.
# 평화롭게 컨텐츠를 진행하던 중, EJN의 Twitch 스트리머 후원 서비스인 Twip으로 미션 하나가 들어왔다.

# 이 미션을 수락하면 캐릭터는 새로운 던전으로 이동하게 됩니다. 던전은 $N$행 $M$열 크기이며 캐릭터는 가장 왼쪽 위의 칸에서 출발합니다.

# 이 던전의 모든 칸에는 아이템이 하나씩 놓여 있고, 각 아이템에는 알파벳이 하나씩 적혀 있습니다. 던전을 탐험하며 주운 아이템들을 주운 순서대로 나열했을 때, 그 문자열이 정확히 제 아이디와 일치하면 가진 아이템들이 모두 없어지고 캐릭터가 한 단계 강화됩니다.

# 던전을 탈출하기 위해서는 숨겨진 포탈을 작동시켜야 합니다. 캐릭터를 던전의 가장 오른쪽 아래 칸에 위치시킨 뒤, “ALL PERFECT”를 외치면 숨겨진 포탈이 작동할 것입니다. 단, 캐릭터가 아이템을 하나라도 가지고 있다면 포탈은 작동하지 않습니다.

# 캐릭터를 한 번 강화시킬 때마다 미션 상금으로  $1$억 원씩이 추가됩니다. 행운을 빕니다!

# “$1$억 원?!” 상금에 큰 감명을 받은 에리는 당장 미션을 수락했다. 그리고 방해되는 시청자들을 제거하기 위해 자신만 채팅을 칠 수 있도록 채팅방을 얼려 버렸다.

# 이제 남은 것은 최대한 많은 상금을 얻으면서 던전을 탈출할 수 있는 이동 방법을 찾고, 한 글자씩 채팅으로 입력하는 것뿐이다. 에리를 도와 주면 상금을 조금 나눠 줄지도 모르니, 그러한 이동 방법을 찾아 주자.


import sys
from collections import deque

N,M,S = map(int,sys.stdin.readline().split())

graph = []
for i in range(N):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)

ch = sys.stdin.readline().rstrip()

cha = {}
for i in ch:
    if i in cha:
        cha[i] += 1
    else:
        cha[i] = 1

ma = {}

for i in range(N):
    for j in range(M):
        if graph[i][j] in cha:
            if graph[i][j] in ma:
                ma[graph[i][j]][0] += 1
            else:
                ma[graph[i][j]] = [1]
            ma[graph[i][j]].append((i,j))


C = 99999999

for i in cha.keys():
    if i in ma:
        C = min(C,ma[i][0]//cha[i])
    else:
        C = 0
        break

ans = deque()

for i in range(C):
    for j in ch:
        ans.append(ma[j].pop())

ans.append((N-1,M-1))

x = 0
y = 0

s = 0
an = []
while ans:
    tx,ty = ans.popleft()
    if tx > x:
        for i in range(tx-x):
            an.append('D')
            s += 1
    elif tx < x:
        for i in range(x-tx):
            an.append('U')
            s += 1
    if ty > y:
        for i in range(ty-y):
            an.append('R')
            s += 1
    elif ty < y:
        for i in range(y-ty):
            an.append('L')
            s += 1
    an.append('P')
    s += 1
    x = tx
    y = ty
an.pop()
s -=1
print(C,s)
for i in an:
    print(i,end='')