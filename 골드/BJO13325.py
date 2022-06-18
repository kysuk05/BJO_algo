# 각 에지에 양수인 가중치가 부여된 높이가 k인 포화이진트리가 주어져 있다. 높이 k인 포화이진트리는 2k개의 리프를 포함하여 (2k+1 − 1)개의 노드를 가진다. 루트에서 어떤 리프까지의 거리는 루트에서 그 리프까지의 경로상에 있는 모든 에지들의 가중치를 더한 값이다. 이 문제에서는, 어떤 에지들의 가중치를 증가시켜서 루트에서 모든 리프까지의 거리가 같도록 하고, 또한 에지 가중치들의 총합을 최소화 하려고 한다.

# 예를 들어, 그림 1(a)에 있는 높이 2 인 포화이진트리를 살펴보자. 에지 옆에 있는 수는 그 에지의 가중치를 나타낸다. 이 경우에 대한 답이 그림 1(b)에 나타나 있다. 즉, 루트에서 모든 리프까지의 거리가 5 이고, 에지 가중치들의 총합은 이 경우에 가능한 최솟값인 15 이다. 



# 그림 1. 에지 가중치를 증가시키는 예.

# 포화이진트리에 들어 있는 모든 에지들의 가중치가 주어졌을 때, 어떤 에지들의 가중치를 증가시켜서 루트에서 모든 리프까지의 거리가 같게 하면서 에지 가중치들의 총합이 최소가 되도록 하는 프로그램을 작성하시오.


import sys

n = int(sys.stdin.readline())

tree = [[]for i in range(n)]

leaf = list(map(int,sys.stdin.readline().split()))

k = 0
t = 2
for i in range(n):
    for j in range(k,t):
        tree[i].append(leaf[j])
    k = j+1
    t = t+2**(i+2)




ans = 0
for i in range(len(tree)):
    ans += sum(tree[i])

for i in range(len(tree)-1,-1,-1):
    for j in range(0,len(tree[i]),2):
        ans += abs(tree[i][j]-tree[i][j+1])
        tree[i][j] = max(tree[i][j],tree[i][j+1])
        tree[i][j+1] = tree[i][j]
        tree[i-1][j//2] += tree[i][j]

print(ans)