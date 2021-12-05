# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.


import sys
n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
en = 0
su = 0
an = 0
for j in range(len(li)):
    while su < m and en < len(li):
        su += li[en]
        en += 1
    if su == m:
        an += 1
    su -= li[j]
print(an)