# 백준이는 국방의 의무를 수행하기 위해 떠났다. 혹독한 훈련을 무사히 마치고 나서, 정말 잘 생겼고 코딩도 잘하는 백준은 그 특기를 살려 적군의 진영을 수학적으로 분석하는 일을 맡게 되었다.

# 2차원 평면 위의 N곳에 적군의 진영이 설치되어 있다. 각 적군의 진영들은 진영마다 하나의 통신탑을 설치해, i번째 적군의 통신탑은 설치 위치로부터 Ri 이내 거리에 포함되는 모든 지역을 자신의 통신영역 Ai로 가지게 된다. 만약 임의의 통신영역 Ai와 Aj가 닿거나 겹치는 부분이 있다면 진영 i와 진영 j는 직접적으로 통신이 가능하다. 
# 물론 직접적으로 통신이 가능하지 않더라도, 임의의 지역 i와 j가 중간에 몇 개의 직접통신을 거쳐서 최종적으로 통신이 가능하다면 i와 j는 상호간에 통신이 가능한 것으로 본다.

# 적들은 영리해서, 상호간에 통신이 가능한 부대끼리는 결집력있는 한 그룹처럼 행동한다. 백준은 이러한 그룹의 개수를 알아내 아군의 전략지침에 도움을 주고자 한다. 군대에 가서도 코딩하는 불쌍한 백준을 위해 적군의 통신망 분석을 도와주자!

import sys
from collections import Counter


def find_parent(parent,x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent,parent[x])
        return parent[x]

def union(parent,x,y):
    x = find_parent(parent,x)
    y = find_parent(parent,y)
    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    parent = [0]*(N)
    for i in range(N):
        parent[i] = i
    
    tower = []
    
    for i in range(N):
        x,y,R = map(int,sys.stdin.readline().split())
        tower.append((x,y,R))
    
    for i in range(N):
        for j in range(i):
            if (tower[i][0]-tower[j][0])**2 + (tower[i][1]-tower[j][1])**2 <= (tower[i][2]+tower[j][2])**2 and parent[i] != parent[j]:
                union(parent,i,j)
    
    for i in range(N):
        find_parent(parent,i)

    print(len(Counter(parent)))