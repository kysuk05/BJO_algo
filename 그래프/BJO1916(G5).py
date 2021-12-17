# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

# 입력
# 첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

# 그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.


#다익스트라 알고리즘

import sys
import heapq

inf = sys.maxsize

n = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
graph = [[]for i in range(n+1)]
pay = [inf]*(n+1)

for i in range(bus):
    st,en,mo = map(int,sys.stdin.readline().split())
    graph[st].append((mo,en))

st,en = map(int,sys.stdin.readline().split())

pay[st] = 0
heap = []
heapq.heappush(heap,(0,st))
def check():
    while heap:
        mo,ne = heapq.heappop(heap)
        if ne!= st and pay[ne] <= mo:
            continue
        if pay[ne] > mo:
            pay[ne] = mo
        for money,next in graph[ne]:
            if mo+money >= pay[en]:
                continue
            else:
                heapq.heappush(heap,(mo+money,next))

check()
print(pay[en])