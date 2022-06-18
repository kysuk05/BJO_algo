# 안형찬 교수님은 알고리즘 분석 기말고사를 준비하려고 한다.

# 알고리즘 기말고사는 총 M분 동안 쉬는 시간 없이 볼 예정이며, 인원이 너무 많아서 공학관 C040호에서 말고 다른 강의실에서 시험을 치를 수 없게 되었다.

# 공학관 C040호는 0분부터 S분까지 사용 가능하다. S는 무조건 M 이상이기 때문에 안 교수님은 별문제 없이 시험을 치를 것으로 생각하였다. 그러나 공학과 C040호에는 다른 시험도 예정되어 있어서 겹치지 않는 시간을 잡아야 한다.

# 각 시험은 xi분에 시작해서 yi분 동안 진행하며 서로 겹치지 않는다. 한 시험이 끝난 직후 다음 시험이 있는 경우도 겹치지 않는 것으로 판단한다. 즉, xi + yi ≤ xj 일 때 i 시험과 j 시험은 서로 겹치지 않는다.

# 안형찬 교수님이 시험을 언제 치를 수 있는지 구해보자.

import sys

N,M,S = map(int,sys.stdin.readline().split())

arr = []

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    arr.append((a,b))

arr.sort()

ans = -1
for i in range(len(arr)-1):
    if arr[i+1][0]-(arr[i][1]+arr[i][0]) >= M:
        ans = arr[i][1]+arr[i][0]
        break

if ans == -1 and S-(arr[-1][1]+arr[-1][0]) >= M:
    ans = arr[-1][1]+arr[-1][0]


if arr[0][0] >= M:
    ans = 0
print(ans)