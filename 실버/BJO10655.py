# 농장에 있는 젖소들이 건강하지 못하다고 생각한 농부 존은 젖소들을 위한 마라톤 대회를 열었고, 농부 존의 총애를 받는 젖소 박승원 역시 이 대회에 참가할 예정이다.

# 마라톤 코스는 N (3 ≤ N ≤ 100000) 개의 체크포인트로 구성되어 있으며, 1번 체크포인트에서 시작해서 모든 체크 포인트를 순서대로 방문한 후 N번 체크포인트에서 끝나야지 마라톤이 끝난다. 게으른 젖소 박승원은 막상 대회에 참가하려 하니 귀찮아져서 중간에 있는 체크포인트 한개를 몰래 건너뛰려 한다. 단, 1번 체크포인트와 N번 체크포인트를 건너뛰면 너무 눈치가 보이니 두 체크포인트는 건너뛰지 않을 생각이다.

# 젖소 박승원이 체크포인트 한개를 건너뛰면서 달릴 수 있다면, 과연 승원이가 달려야 하는 최소 거리는 얼마일까?

# 참고로, 젖소 마라톤 대회는 서울시내 한복판에서 진행될 예정이기 때문에 거리는 택시 거리(Manhattan Distance)로 계산하려고 한다. 즉, (x1,y1)과 (x2,y2) 점 간의 거리는 |x1-x2| + |y1-y2| 로 표시할 수 있다. (|x|는 절댓값 기호다.)


import sys

n = int(sys.stdin.readline())

arr = []

gap = 0

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr.append((x,y))

for i in range(n-2):
    gap = max(abs(arr[i+1][0]-arr[i+2][0])+abs(arr[i][0]-arr[i+1][0])+abs(arr[i][1]-arr[i+1][1])+abs(arr[i+1][1]-arr[i+2][1])-abs(arr[i][0]-arr[i+2][0])-abs(arr[i][1]-arr[i+2][1]),gap)

ans = 0
a,b = arr[0]
for i in range(1,n):
    x,y = arr[i]
    ans += abs(a-x)+abs(b-y)
    a = x
    b = y
print(ans - gap)