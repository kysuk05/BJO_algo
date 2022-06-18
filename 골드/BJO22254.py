# 거듭된 창업 성공을 이룬 류진국 사장은 이번에는 맞춤형 선물을 제작해주는 공장을 만들기로 했다. 현재 들어온 맞춤형 선물 주문은 총 $N$개이며, 각 맞춤형 선물마다 제작에 필요한 시간이 정해져있다. 주문의 번호는 $1$번부터 $N$번까지 매겨져 있으며, 다음과 같은 규칙에 맞게 공정이 이뤄진다.

# 공정 라인이 총 $K$개가 있다면 $1$번부터 $K$번까지의 번호가 존재한다.
# 공정 라인의 사용 시간은 배정된 맞춤형 선물들의 제작 시간의 총합이다.
#  $i$번 선물은 $1$번 부터 $i-1$번 선물들이 배정된 이후에 사용 시간이 가장 적은 공정 라인 중 하나에 배정된다.
# 모든 맞춤형 선물의 제작이 완료될 때까지 최대 $X$시간이 남아있는 상황인데, 아직 공정 라인의 개수 $K$가 정해져 있지 않다. 류진국 사장은 이 분야 최고 권위자, 공정 컨설턴트 호석에게 의뢰했다. 공정 컨설턴트 호석은 최소한의 비용을 쓰기 위해서 공정 라인의 개수를 최소화 시키고자 한다. 호석을 도와 필요한 최소 공정 라인 개수를 계산하자

import sys
import heapq

N,X = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

max_num = 100000
min_num = 1

while True:
    if max_num == min_num:
        break
    ans = (max_num+min_num)//2
    line = [0 for i in range(ans)]
    for j in range(N):
        t = heapq.heappop(line)
        t += arr[j]
        heapq.heappush(line,t)
    
    if max(line) <= X:
        max_num = ans
    else:
        min_num = ans+1
print(max_num)