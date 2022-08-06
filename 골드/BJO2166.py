# 2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

import sys
from collections import deque
n = int(sys.stdin.readline())

x = deque()
y = deque()
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)

temp = y.popleft()
y.append(temp)

ans1 = 0
for i in range(n):
    ans1 += x[i]*y[i]

temp = y.pop()
y.appendleft(temp)
temp = y.pop()
y.appendleft(temp)

ans2 = 0
for i in range(n):
    ans2 += x[i]*y[i]
    

print(abs(ans1-ans2)/2)
