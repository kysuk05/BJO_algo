# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.


import sys

n,m = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

an = 100000000
su = 0
en = 0
for i in range(n):
    while su < m and en < n:
        su += li[en]
        en += 1
    if su >= m:
        if en - i < an:
            an = en - i
        su -= li[i]

if an == 100000000:
    print(0)
else:
    print(an)