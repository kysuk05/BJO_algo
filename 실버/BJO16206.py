# 오늘은 재현이의 생일이다. 재현이는 친구 N명에게 롤케이크를 1개씩 선물로 받았다. 롤케이크의 길이는 A1, A2, ..., AN이다. 재현이는 길이가 10인 롤케이크만 먹는다. 따라서, 롤케이크를 잘라서 길이가 10인 롤케이크를 최대한 많이 만들려고 한다.

# 롤케이크는 다음과 같은 과정을 통해서 자를 수 있다.

# 자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자를 수 있다. 이때, 고른 롤케이크의 길이를 x라고 한다.
# 0보다 크고, x보다 작은 자연수 y를 고른다.
# 롤케이크를 잘라 길이가 y, x-y인 롤케이크 두 개로 만든다.
# 재현이는 롤케이크를 최대 M번 자를 수 있다. 이때, 만들 수 있는 길이가 10인 롤케이크 개수의 최댓값을 구하는 프로그램을 작성하시오.

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

roll = list(map(int,sys.stdin.readline().split()))

cake = []
lef = []

ans = 0

for i in roll:
    if i == 10:
        ans += 1
    elif i % 10 == 0:
        cake.append(i)
    else:
        lef.append(i)



cake.sort()
lef.sort()

cake = deque(cake)
lef = deque(lef)


while cake:
    t = cake.popleft()
    k = (t//10)-1
    if k <= m:
        m -= k
        ans += k+1
    else:
        ans += m
        m = 0
    if m == 0:
        break

while lef:
    t = lef.popleft()
    k = (t//10)
    if k <= m:
        m -= k
        ans += k
    else:
        ans += m
        m = 0
    if m == 0:
        break
print(ans)