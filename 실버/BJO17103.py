# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 
# 두 소수의 순서만 다른 것은 같은 파티션이다.

import sys


li = [True]*(1000000)
for i in range(2,1000000):
    an = i
    an = an**2
    while an < 1000000:
        li[an] = False
        an+=i
li[0] = False
li[1] = False
n = int(sys.stdin.readline())

for i in range(n):
    ans = 0
    t = int(sys.stdin.readline())
    for j in range(2,(t//2)+1):
        if li[j] and li[t-j]:
            ans += 1
    print(ans)
            