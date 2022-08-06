# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.


import sys

n,m = map(int,sys.stdin.readline().split())

se = set()

for i in range(n):
    se.add(sys.stdin.readline().rstrip())

ans = 0

for j in range(m):
    k = sys.stdin.readline().rstrip()
    if k in se:
        ans += 1
print(ans)