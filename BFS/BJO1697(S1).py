# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.



from collections import deque


n,k = map(int,input().split())

queue = deque()
queue.append(n)
graph = [0]*100001
def bfs():
    while queue:
        n = queue.popleft()
        n1 = n-1
        n2 = n+1
        n3 = n*2
        if n == k:
            return(graph[n])
        if n1<0 or graph[n1] != 0:
            pass
        else:
            graph[n1] = graph[n]+1
            queue.append(n1)
        
        if n2 > 100000:
            continue
        if n2<0 or graph[n2] != 0:
            pass
        else:
            graph[n2] = graph[n]+1
            queue.append(n2)
        
        if n3 > 100000:
            continue
        if n3<0 or graph[n3] != 0:
            pass
        else:
            graph[n3] = graph[n]+1
            queue.append(n3)


print(bfs())