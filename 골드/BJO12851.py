# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

from collections import deque
graph = [0]*200000

n,k = map(int,input().split())

qu = deque()
qu.append(n)
graph[n] = 1
cnt = 0
check = 0
while qu:
    x = qu.popleft()
    if (check == 0) and (x == k):
        check = 1
        ans = graph[x]
        cnt += 1
    elif x == k:
        if ans == graph[x]:
            cnt += 1
    if (check == 1) and (ans != graph[x]):
        break
    if x > k:
        if (graph[x-1] == 0) or (graph[x-1] == graph[x]+1):
            graph[x-1] = graph[x]+1
            qu.append(x-1)
    else:
        if (x-1 >= 0) and ((graph[x-1] == 0) or (graph[x-1] == graph[x]+1)):
            graph[x-1] = graph[x]+1
            qu.append(x-1)
        if (x*2) < 200000:
            if(graph[x*2] == 0) or (graph[x*2] == graph[x]+1):
                graph[x*2] = graph[x]+1
                qu.append(x*2)
        if graph[x+1] == 0 or (graph[x+1] == graph[x]+1):
            graph[x+1] = graph[x]+1
            qu.append(x+1)
print(ans-1)
print(cnt)
