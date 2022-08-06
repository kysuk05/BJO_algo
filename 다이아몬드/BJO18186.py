# 라면매니아 교준이네 집 주변에는 N개의 라면 공장이 있다. 각 공장은 1번부터 N번까지 차례대로 번호가 부여되어 있다. 교준이는 i번 공장에서 정확하게 Ai개의 라면을 구매하고자 한다(1 ≤ i ≤ N).

# 교준이는 아래의 세 가지 방법으로 라면을 구매할 수 있다.

# i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다.
# i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
# i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.
# 최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성하시오.


import sys

n,b,c = map(int,sys.stdin.readline().split())
graph = list(map(int,sys.stdin.readline().split()))
ans = 0

idx = 0

if b <= c:
    ans = sum(graph)*b
else:    
    while idx < n:
        if idx+2< n:
            if graph[idx+1]-graph[idx+2] > 0:
                temp = min(graph[idx], graph[idx+1]-graph[idx+2])
                ans += temp*(b+c)
                graph[idx] -= temp
                graph[idx+1] -= temp
            temp = min(graph[idx],graph[idx+1],graph[idx+2])
            ans += temp*(b+2*c)
            graph[idx] -= temp
            graph[idx+1] -= temp
            graph[idx+2] -= temp
        if idx+1 < n:
            temp = min(graph[idx],graph[idx+1])
            ans += temp*(b+c)
            graph[idx] -= temp
            graph[idx+1] -= temp
        ans += graph[idx]*b
        idx += 1
print(ans)