# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.





import sys

n,m = map(int,sys.stdin.readline().split())

lis = sorted(map(int,sys.stdin.readline().split()))
li = []
check = set()
che = [0]*10
def func(k):
    if k == m:
        ap = tuple(li)
        a = len(check)
        check.add(ap)
        if a != len(check):
            for i in range(len(li)):
                print(li[i],end=' ')
            print()
        return
    for j in range(n):
        if che[j] == 0:
            if li and lis[j] < li[-1]:
                continue
            li.append(lis[j])
            che[j] = 1
            func(k+1)
            che[j] = 0
            li.pop()

func(0)
