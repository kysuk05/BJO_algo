# 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.

# 입력
# 첫 번째 줄에는 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)

# 두 번째 줄에는 수열을 나타내는 N개의 정수가 주어진다. 수열에 나타나는 수는 모두 1 이상 100,000 이하이다.


import sys
from collections import deque
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

qu = deque()
dic = dict()
ans = 0
for i in range(n):
    if li[i] in dic and dic[li[i]] > 0:
        while qu[0] != li[i]:
            k = qu.popleft()
            dic[k] -= 1 
        k = qu.popleft()
        dic[k] -= 1 
    qu.append(li[i])
    if li[i] in dic:
        dic[li[i]]+=1
    else:
        dic[li[i]]=1
    ans += len(qu)
print(ans)