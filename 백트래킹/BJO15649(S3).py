# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

#백트래킹을 이용한 풀이
n,m = map(int,input().split())
lis = [0]*10
isused = [0]*10
def func(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    for i in range(n):
        if isused[i] == 0:
            lis[k] = i+1
            isused[i] = 1
            func(k+1)
            isused[i] = 0
            

func(0)



#인터넷에 찾아보니 파이썬에서는 내장함수로 permutation을 지원한다.
print('내장함수')
from itertools import permutations

li = map(str,range(1,n+1))

ans = (list(map(' '.join,permutations(li,m))))

for i in range(len(ans)):
    print(ans[i])