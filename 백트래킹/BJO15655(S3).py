# N개의 자연수와 자연수 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 
# N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.



import sys

n,m = map(int,sys.stdin.readline().split())

lis = sorted(map(int,sys.stdin.readline().split()))
li = []
isused = [0]*10

def func(k):
    if k == m:
        for i in range(m):
            print(li[i],end=' ')
        print()
        return
    
    for j in lis:
        if li:
            if j not in li and li[-1] < j:
                li.append(j)
                func(k+1)
                li.pop()
        else:
            li.append(j)
            func(k+1)
            li.pop()

func(0)