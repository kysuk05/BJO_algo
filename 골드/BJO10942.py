# 첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.

# 둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.

# 셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.

# 넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.


import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

li = list(sys.stdin.readline().split())

dyn = [[-1 for i in range(n)]for i in range(n)]
def solve(i,j):
    if dyn[i][j] != -1:
        return dyn[i][j]
    if i == j:
        dyn[i][j] = 1
    elif i == j-1:
        if li[i] == li[j]:
            dyn[i][j] = 1
        else:
            dyn[i][j] = 0
    else:
        if li[i] == li[j]:
            dyn[i][j] = solve(i+1,j-1)
        else:
            dyn[i][j] = 0
    return dyn[i][j]
        


m = int(sys.stdin.readline())

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(solve(a-1,b-1))

    