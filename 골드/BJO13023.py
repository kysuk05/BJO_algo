# BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

# 오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

import sys
from collections import deque


N,M = map(int,sys.stdin.readline().split())

li = [[]for i in range(N)]


for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    li[a].append(b)
    li[b].append(a)

ans = 0
def dfs():
    global ans
    if len(lis) == 5:
        ans = 1
        return
    else:
        for j in li[lis[-1]]:
            if j not in lis:
                lis.append(j)
                dfs()
                lis.pop()


for i in range(N):
    if li[i]:
        check = [0]*(N)
        check[i] = 1
        for j in li[i]:
            lis = []
            lis.append(j)
            check[j] = check[i]+1
            dfs()
            if ans == 1:
                break
    if ans == 1:
        break    

print(ans)