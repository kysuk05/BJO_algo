# 어젯밤 겨울 캠프 장소에서 월드 본원까지 이어지는, 
# 흙으로 된 비밀길 위에 폭우가 내려서 N (1 <= N <= 10,000) 개의 물웅덩이가 생겼다. 
# 월드학원은 물웅덩이를 덮을 수 있는 길이 L (L은 양의 정수) 짜리 널빤지들을 충분히 가지고 있어서, 이들로 다리를 만들어 물웅덩이들을 모두 덮으려고 한다. 
# 물웅덩이들의 위치와 크기에 대한 정보가 주어질 때, 
# 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 구하여라.


import sys
from collections import deque

N,L = map(int,sys.stdin.readline().split())


pools = []

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    pools.append((x,y))

pools.sort()

pools = deque(pools)
cnt = 0
st = 0

while pools:
    x,y = pools.popleft()
    if x < st:
        x = st
    if x >= y:
        continue
    if (y-x)%L == 0:
        cnt += (y-x)//L
        st = y
    else:
        cnt += (y-x)//L+1
        st = y+L-(y-x)%L

print(cnt)