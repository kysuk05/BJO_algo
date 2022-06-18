# 컴공 출신은 치킨집을 하게 되어있다. 현실을 부정하지 말고 받아들이면 마음이 편하다. 결국 호석이도 2050년에는 치킨집을 하고 있다. 치킨집 이름은 "호석이 두마리 치킨"이다.

# 이번에 키친 도시로 분점을 확보하게 된 호석이 두마리 치킨은 도시 안에 2개의 매장을 지으려고 한다. 도시는 N 개의 건물과 M 개의 도로로 이루어져 있다. 건물은 1번부터 N번의 번호를 가지고 있다. i 번째 도로는 서로 다른 두 건물 Ai 번과 Bi 번 사이를 1 시간에 양방향으로 이동할 수 있는 도로이다.

# 키친 도시에서 2개의 건물을 골라서 치킨집을 열려고 한다. 이 때 아무 곳이나 열 순 없어서 모든 건물에서의 접근성의 합을 최소화하려고 한다. 건물 X 의 접근성은 X 에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단 시간이다. 즉, "모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합"을 최소화할 수 있는 건물 2개를 골라서 치킨집을 열려고 하는 것이다.

# 컴공을 졸업한 지 30년이 넘어가는 호석이는 이제 코딩으로 이 문제를 해결할 줄 모른다. 알고리즘 퇴물 호석이를 위해서 최적의 위치가 될 수 있는 건물 2개의 번호와 그 때의 "모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합"을 출력하자. 만약 이러한 건물 조합이 여러 개라면, 건물 번호 중 작은 게 더 작을수록, 작은 번호가 같다면 큰 번호가 더 작을수록 좋은 건물 조합이다.

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [[]for i in range(n+1)]

qu = deque()

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [(100000,100000,100000)]

for i in range(1,n):
    for j in range(i+1,n):
        check = [-1 for i in range(n+1)]
        check[i] = 0
        check[j] = 0
        qu.append(i)
        qu.append(j)
        while qu:
            x = qu.popleft()
            for k in graph[x]:
                if check[k] != -1:
                    continue
                check[k] = check[x]+2
                qu.append(k)
        if sum(check) < ans[-1][-1]:
            ans.append((i,j,sum(check)))
if n != 2:
    print(ans[-1][0],ans[-1][1],ans[-1][2]+1)
else:
    print(1,2,0)