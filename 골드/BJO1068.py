# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

# 예를 들어, 다음과 같은 트리가 있다고 하자.

# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.

# 이제 리프 노드의 개수는 1개이다.


import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for i in range(n)]


t = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    if t[i] == -1:
        st = i
    else:
        graph[t[i]].append(i)

x = int(sys.stdin.readline())

di = {}
qu = deque()

qu.append((x))
while qu:
    t = qu.popleft()
    di[t] = 0
    if graph[t]:
        for i in graph[t]:
            qu.append((i))



ans = 0
for i in graph[st]:
    if i in di:
        if len(graph[st]) == 1:
            ans += 1
            break
        continue
    qu.append((i))

while qu:
    t = qu.popleft()
    if graph[t]:
        for i in graph[t]:
            if i in di:
                if len(graph[t]) == 1:
                    ans += 1
                continue
            qu.append(i)
    else:
        if t in di:
            continue
        ans+=1
        
print(ans)