# 이하는 최근 사과나무 씨앗을 구매하여 농장 뒷뜰에 일렬로 $1$번부터 $N$번까지 심었다. 이 나무들의 초기 높이는 모두 $0$이다.

# 사과나무를 무럭무럭 키우기 위해 이하는 물뿌리개 $2$개를 준비했다. 한 물뿌리개는 나무 하나를 $1$만큼 성장시키고, 다른 물뿌리개는 나무 하나를 $2$만큼 성장시킨다. 이 물뿌리개들은 동시에 사용해야 하며, 물뿌리개를 나무가 없는 토양에 사용할 수는 없다. 두 물뿌리개를 한 나무에 사용하여 $3$만큼 키울 수도 있다.

# 물뿌리개 관리 시스템을 전부 프로그래밍한 이하는 이제 사과나무를 키워보려고 했다. 그 순간, 갊자가 놀러와서 각 사과나무의 높이가 이런 배치가 되었으면 좋겠다고 말했다. 이제 이하는 약간 걱정이 되기 시작했는데, 갊자가 알려준 사과나무의 배치를 이 프로그램 상으로 만들어내지 못할 수도 있기 때문이다.

# 이하는 이제 프로그램을 다시 수정하느라 바쁘기 때문에, 두 물뿌리개를 이용해 갊자가 알려준 사과나무의 배치를 만들 수 있는지의 여부를 판단하는 과정은 여러분의 몫이 되었다.



import sys


n = int(sys.stdin.readline())
from collections import deque

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

cnt = 0
qu = deque(arr)

ans = 'YES'

while qu and qu[0] == 0:
    qu.popleft()

if not qu:
    qu.append(0)

while qu:
    if qu[0] == 1 and qu[-1] >= 2:
        qu.popleft()
        qu[-1] -= 2
    
    if qu[0] != 1:
        if sum(qu) % 3 == 0:
            break
        else:
            ans = 'NO'
            break
    
    if qu[-1] == 0:
        qu.pop()
    
    if qu[-1] == 1:
        if len(qu) < 2 or qu[-2] == 1:
            ans = 'NO'
            break
        else:
            qu.pop()
            qu.appendleft(1)

print(ans)