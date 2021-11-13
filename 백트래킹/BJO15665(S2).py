# N개의 자연수와 자연수 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.



import sys

n,m = map(int,sys.stdin.readline().split())
se = set(map(int,sys.stdin.readline().split()))
se = list(se)
se.sort()

lis = []

def func(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    for j in range(len(se)):
        lis.append(se[j])
        func(k+1)
        lis.pop()

func(0)