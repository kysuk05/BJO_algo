# 홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 도현이를 위해 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.

#  100,000 이하의 양의 정수로 이루어진 길이가 N인 수열이 주어진다.  이 수열에서 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

import sys
from collections import deque


qu = deque()
ans = []
di = {}
n,k = map(int,sys.stdin.readline().split())
lis = list(map(int,sys.stdin.readline().split()))
for i in range(len(lis)):
    if lis[i] in di:
        di[lis[i]] += 1
        qu.append(lis[i])
        if di[lis[i]] > k:
            while True:
                nu = qu.popleft()
                di[nu] -= 1
                if nu == lis[i]:
                    break
        ans.append(len(qu))
    else:
        di[lis[i]] = 1
        qu.append(lis[i])
        ans.append(len(qu))
print(max(ans))