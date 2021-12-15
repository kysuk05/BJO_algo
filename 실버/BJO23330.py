# 수직선에 n개의 점이 찍혀 있다. 각각의 점의 x좌표가 주어졌을 때, n2개의 모든 쌍에 대해서 거리를 더한 값을 구하는 프로그램을 작성하시오.

# 즉, 모든 i, j에 대해서 |x[i] - x[j]|의 합을 구하는 것이다.

# 입력
# 첫째 줄에 n(1 ≤ n ≤ 500,000)이 주어진다. 다음 줄에는 x[1], x[2], x[3], …, x[n]이 주어진다. 각각은 0 이상 10,000,000 이하의 정수이다.

# 출력
# 첫째 줄에 답을 출력한다.

import sys
from collections import deque
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li.sort()

lis = deque()
for i in range(1,len(li)):
  lis.append(li[i]-li[0])

ans = []
su = sum(lis)
ans.append(su)
cn = 0
while len(lis)>1:
    x = lis.popleft()-cn
    su = su-(x*len(lis))-x
    ans.append(su)
    cn = cn+x
print(sum(ans)*2)
          