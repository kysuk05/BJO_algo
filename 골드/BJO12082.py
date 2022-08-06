# As the leader of the Evil League of Evil, Bad Horse has a lot of problems to deal with. Most recently, there have been far too many arguments and far too much backstabbing in the League, so much so that Bad Horse has decided to split the league into two departments in order to separate troublesome members. Being the Thoroughbred of Sin, Bad Horse isn't about to spend his valuable time figuring out how to split the League members by himself. That what he's got you -- his loyal henchman -- for.

import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    dic = {}
    
    qu = deque()
    
    
    ans = 0
    
    for j in range(n):
        x,y = sys.stdin.readline().rstrip().split()
        
        if ans == 1:
            continue
        
        if x in dic:
            dic[x].append(y)
        else:
            dic[x] = [y]
        if y in dic:
            dic[y].append(x)
        else:
            dic[y] = [x]
    
        check = {}
        qu.append((x,0))
        check[x] = 0
        while qu:
            x,t = qu.popleft()
            for k in dic[x]:
                if k == y:
                    if t%2 == 1:
                        ans = 1
                        break
                else:
                    if k not in check:
                        check[k] = 0
                        qu.append((k,t+1))
            if ans == 1:
                break
    if ans == 1:
        print('Case #'+(str(i+1))+': No')
    else:
        print('Case #'+(str(i+1))+': Yes')