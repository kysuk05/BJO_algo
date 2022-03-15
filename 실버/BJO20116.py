# 진수에게는 총 n개의 상자가 있다. 모든 상자는 2L × 2L 크기의 정사각형 모양이고, 상자의 밀도는 균일하다.

# 진수는 이 상자들을 바닥에서부터 차곡차곡 쌓아올린다. 바닥은 y=0 이다.

# 이 상자들을 바닥에 가까이 있는 있는 상자부터 각각 1번, 2번, ..., n번 상자라고 보았을 때 i번 상자의 중심은 (xi, 2L×i - L) 이 되고, 이는 i번 상자 1개의 무게 중심과 같다.

# 위에서 상자의 밀도는 균일하다고 가정하였으므로, 상자 여러 개의 무게 중심을 구하면 각각의 상자들의 무게 중심을 평균 낸 값이 된다.

# 진수는 원하는 중심 좌표에 상자들을 쌓아올릴 때 무너지지 않고 균형을 이루는 지를 알고 싶다.

# 모든 1 ≤ i < n 에 대하여 i+1, i+2, ..., n 번 상자들의 무게 중심의 x좌표가 i번 상자의 구간 안에 포함되면 박스 전체가 균형을 이루게 된다. i번 상자의 구간는 xi-L과 xi+L 사이로 정의하며, xi-L, xi+L은 포함하지 않는다. 따라서 상자 모서리에 걸쳐 있는 경우는 균형을 이루지 않는 것으로 한다.

# n개의 상자들의 중심 좌표가 주어지면, 해당 상자들이 균형을 이루는지 알아내보자.


import sys

n,L = map(int,sys.stdin.readline().split())

boxes = list(map(int,sys.stdin.readline().split()))

ans = 0
total = sum(boxes)

if n == 1:
    print('stable')


else:
    for i in range(n-1):
        total -= boxes[i]
        mid = total / (n-i-1)
        if mid >= boxes[i]+L or mid<=boxes[i]-L:
            ans = 1
            break

if ans == 0:
    print('stable')
else:
    print('unstable')
