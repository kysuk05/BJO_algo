# 구간 $[l,r]$이란, $l$ 이상 $r$ 이하의 모든 실수로 이루어진 집합을 의미한다.

# 구간 $N$개가 주어진다. 이때, 다음과 같은 질의 $Q$개를 해결하는 프로그램을 작성하시오.

# 주어진 $l$과 $r$에 대해, 구간을 $1$개 이상 선택하여 그 교집합이 정확히 $[l,r]$이 되도록 할 수 있는가? 만약 가능하다면, 최소 몇 개의 구간을 선택해야 하는가?

import sys

n = int(sys.stdin.readline())

dic_st = {}
dic_en = {}

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a in dic_st:
        dic_st[a][0][b] = 0
        dic_st[a][1] = max(dic_st[a][1],b)
    else:
        dic_st[a] = [{b:0},b]
    if b in dic_en:
        dic_en[b][0][a] = 0
        dic_en[b][1] = min(dic_en[b][1],a)
    else:
        dic_en[b] = [{a:0},a]



n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    
    if (a not in dic_st) or (b not in dic_en):
        print(-1)
    elif b in dic_st[a][0]:
        print(1)
    elif b < dic_st[a][1] and a > dic_en[b][1]:
        print(2)
    else:
        print(-1)