# 영선이는 총 N개의 정수로 이루어져 있는 배열 A를 가지고 있다.

# 배열에 적용할 수 있는 연산은 다음과 같다.

# A에 있는 수 중 하나를 골라서 K를 더한다.
# 위의 연산은 사용하고 싶은 만큼 사용할 수 있다.

# 배열 A가 주어졌을 때, 연산을 적용해서 1부터 N까지의 수가 모두 하나씩 있는 배열을 만들 수 있는지 없는지 구하는 프로그램을 작성하시오.


import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())

check = [0]*(N+1)

qu = deque(map(int,sys.stdin.readline().split()))

ans = 1

for i in range(len(qu)):
    num = qu.popleft()
    if num > N:
        ans = 0
        break
    if check[num] == 0:
        check[num] = 1
    else:
        qu.append(num)

while ans == 1 and qu:
    num = qu.popleft()
    while num <= N:
        num += K
        if num > N:
            ans = 0
            break
        if check[num] == 0:
            check[num] = 1
            break
        

print(ans)