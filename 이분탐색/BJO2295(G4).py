# N(5 ≤ N ≤ 1,000)개의 자연수들로 이루어진 집합 U가 있다. 이 중에서 적당히 세 수를 골랐을 때, 그 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다. 이러한 경우들 중에서, 가장 큰 d를 찾으라.

# 예를 들어 {2, 3, 5, 10, 18}와 같은 집합이 있다고 하자. 2+3+5 = 10이 되고, 이 수는 집합에 포함된다. 하지만 3+5+10 = 18이 되고, 이 경우가 세 수의 합이 가장 커지는 경우이다.


import sys
from itertools import combinations
n = int(sys.stdin.readline())

li=set()
for i in range(n):
    li.add(int(sys.stdin.readline()))
li = sorted(list(li))
li2 = list(combinations(li,2))
se = set()
for j in range(len(li2)):
    x,y = li2[j]
    se.add(x+y)
    se.add(x+x)
    se.add(y+y)

nli = list(se)
nli.sort()
for a in range(n-1,-1,-1):
    check = 0
    for b in nli:
        if li[a] - b in li:
            check = 1
            print(li[a])
            break
    if check == 1:
        break

