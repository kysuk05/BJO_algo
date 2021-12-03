# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

import sys
sys.setrecursionlimit(10**6)
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


n,m = map(int,input().split())

k = (fac(n)//fac(m))//fac(n-m)
print(k%10007)