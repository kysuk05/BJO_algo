# N개의 자연수와 자연수 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 
# N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.



import sys

n,m = map(int,sys.stdin.readline().split())
lis = sorted(map(int,sys.stdin.readline().split()))

li = []

def func(k):
    if k == m:
        for i in range(m):
            print(li[i],end=' ')
        print()
        return
    for j in lis:
        if li:
            if li[-1] <= j:
                li.append(j)
                func(k+1)
                li.pop()
        else:
            li.append(j)
            func(k+1)
            li.pop()
        

func(0)