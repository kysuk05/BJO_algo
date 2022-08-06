# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 자연수 중에 금민수인 것의 개수를 출력하는 프로그램을 작성하시오.

import sys
from collections import deque

n,m = map(str,sys.stdin.readline().split())

su = deque(['4','7'])
kum = []
while su:
    t = su.popleft()
    a = t + '4'
    b = t + '7'
    if len(t) > len(m):
        break
    elif len(t) >= len(n):
        kum.append(t)
    su.append(a)
    su.append(b)




n = int(n)
m = int(m)


ans = 0
while kum:
    t = kum.pop()
    if int(t) >= n and int(t) <= m:
        ans += 1

print(ans)

