# 개구리가 일렬로 놓여 있는 징검다리 사이를 폴짝폴짝 뛰어다니고 있다. 징검다리에는 숫자가 각각 쓰여 있는데, 이 개구리는 매우 특이한 개구리여서 어떤 징검다리에서 점프를 할 때는 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.

# 이 개구리는 a번째 징검다리에서 b번째 징검다리까지 가려고 한다. 
# 이 개구리가 a번째 징검다리에서 시작하여 최소 몇 번 점프를 하여 b번째 징검다리까지 갈 수 있는지를 알아보는 프로그램을 작성하시오.


import sys
from collections import deque

n = int(sys.stdin.readline())

br = list(map(int,sys.stdin.readline().split()))

st,en = map(int,sys.stdin.readline().split())

st -= 1
en -= 1

qu = deque()

check = [0]*n



check[st] = 1
qu.append(st)

ans = -1

while qu:
    x = qu.popleft()
    if x == en:
        ans = check[x]-1
        break
    
    temp = x
    while temp+br[x] < n:
        temp += br[x]
        if check[temp] == 0:
            check[temp] = check[x]+1
            qu.append(temp)
    temp = x
    while temp - br[x] >= 0:
        temp -= br[x]
        if check[temp] == 0:
            check[temp] = check[x]+1
            qu.append(temp)

print(ans)