# 처음에 0이 하나 포함되어있는 배열 A가 있다. 이때, 다음 쿼리를 수행해야 한다.

# 1 x: A의 가장 뒤에 x를 추가한다.
# 2 x: A에서 x를 제거한다. A에 x가 두 개 이상 있는 경우에는 가장 앞에 있는 하나만 제거한다. 항상 A에 x가 있는 쿼리만 주어진다.
# 3: A에 포함된 모든 원소를 더한 값을 출력한다.
# 4: A에 포함된 모든 원소를 XOR한 값을 출력한다.

import sys

M = int(sys.stdin.readline())
total = 0
tot_xor = 0

for i in range(M):
    t = sys.stdin.readline()
    if t[0] in ('1','2'):
        a,b = map(int,t.split())
        if a == 1:
            total += b
            tot_xor ^= b
        else:
            total -= b
            tot_xor ^= b
    elif t[0] == '3':
        print(total)
    else:
        print(tot_xor)