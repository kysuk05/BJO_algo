# 그래프는 정점과 간선으로 이루어져 있다. 두 정점 사이에 경로가 있다면, 두 정점은 연결되어 있다고 한다. 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다.

# 트리는 사이클이 없는 연결 요소이다. 트리에는 여러 성질이 있다. 예를 들어, 트리는 정점이 n개, 간선이 n-1개 있다. 또, 임의의 두 정점에 대해서 경로가 유일하다.

# 그래프가 주어졌을 때, 트리의 개수를 세는 프로그램을 작성하시오.


import sys

def dfs(pre,n):
    check[n] = 1
    for i in tree[n]:
        if i == pre:
            continue
        if check[i] != 0:
            return 0
        if dfs(n,i) != 1:
            return 0
    return 1
        
            
        
        
case = 1
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    tree = [[]for i in range(a+1)]
    check = [0]*(a+1)
    
    for i in range(b):
        x,y = map(int,sys.stdin.readline().split())
        tree[x].append(y)
        tree[y].append(x)
    
    ans = 0
    
    
    for i in range(1,len(tree)):
        if check[i] == 0:
            ans += dfs(0,i)
    
    if ans > 1:
        print('Case',str(case)+': A forest of',ans,'trees.')
    elif ans == 1:
        print('Case',str(case)+': There is one tree.')
    else:
        print('Case',str(case)+': No trees.')
    
    case += 1
        
        