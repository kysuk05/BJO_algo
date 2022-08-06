# 희현이는 원장선생님 말씀에 토를 다는 것을 몹시 좋아한다. 토를 단다는 것은 원장선생님께서 어떤 단어를 말씀하시면 그 단어의 맨 앞이나 중간, 혹은 맨 뒤에 한 글자를 끼워 넣어서 새로운 단어를 만드는 것으로, 버릇없는 행동과는 아무런 관계가 없는 순수한 단어 놀이이다.

# 희현이는 사전에 등재된 단어만을 사용한다. 사전은 d개의 단어로 구성되어 있으며, 각 단어는 80자 이내의 알파벳 소문자로만 이루어져 있다. 희현이는 원장선생님께서 어떤 단어를 말씀하셨을 때, 한 글자씩 토를 달아 사전에 등재된 단어를 계속 만들어 갈 경우, 가장 긴 단어를 만들려면 어떻게 해야 하는지가 궁금해졌다. 이를 해결하는 프로그램을 작성하라.

import sys
from collections import deque

n,s = sys.stdin.readline().split()

dic = {}
for i in range(int(n)):
    k = sys.stdin.readline().rstrip()
    if len(k) in dic:
        dic[len(k)].append(k)
    else:
        dic[len(k)] = [k]


qu = deque()

qu.append(s)
while qu:
    x = qu.popleft()
    if len(x)+1 not in dic:
        break
    for i in dic[len(x)+1]:
        cnt = 0
        a = 0
        b = 0
        while a < len(x) and b < len(i):
            if x[a] != i[b]:
                b += 1
                cnt += 1
            else:
                a += 1
                b += 1
            if cnt > 1:
                break
        if cnt <= 1:
            dic[len(x)+1].remove(i)
            qu.append(i)

print(x)