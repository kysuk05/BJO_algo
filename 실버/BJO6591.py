# n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

import sys
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    if a-b < b:
        b = a-b
    ans = 1
    for i in range(a,a-b,-1):
        ans *= i
    for i in range(1,b+1):
        ans //=i
    print(ans)