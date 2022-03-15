# 간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
# 만약 이 문제를 해결하는 데에 어려움이 있다면, 하단의 힌트에 첨부한 문서를 참고하자.


import sys
sys.setrecursionlimit(10**6)

N,R,Q = map(int,sys.stdin.readline().split())

dp = [0 for i in range(N+1)]
tree = [[]for i in range(N+1)]
check = [0 for i in range(N+1)]
for i in range(N-1):
    U,V = map(int,sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

def dfs(n):
    if check[n] != 0:
        return dp[n]
    else:
        check[n] = 1
        dp[n] = 1
        for i in tree[n]:
            if check[i] == 0:
                dp[n] += dfs(i)
        return dp[n]

dfs(R)


for i in range(Q):
    print(dp[int(sys.stdin.readline())])