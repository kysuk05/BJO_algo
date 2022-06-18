# 9학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다. 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다. 그런 준석이에게도 희망이 있다. 바로 친구비다!

# 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다. 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다. 그래서 준석이는 “친구의 친구는 친구다”를 이용하기로 했다.

# 준석이는 이제 모든 친구에게 돈을 주지 않아도 된다!

# 위와 같은 논리를 사용했을 때, 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구하라.

import sys
from collections import deque

N,M,k = map(int,sys.stdin.readline().split())

friend = [[]for i in range(N+1)]
check = [0 for i in range(N+1)]
qu = deque()

f_m = list(map(int,sys.stdin.readline().split()))

for i in range(M):
    v,w = map(int,sys.stdin.readline().split())
    friend[v].append(w)
    friend[w].append(v)

ans = 0
for i in range(1,N+1):
    if check[i] == 0:
        check[i] = 1
        min_money = f_m[i-1]
        for j in friend[i]:
            if check[j] == 0:
                check[j] = 1
                qu.append(j)
        while qu:
            x = qu.popleft()
            min_money = min(min_money,f_m[x-1])
            for j in friend[x]:
                if check[j] == 0:
                    check[j] = 1
                    qu.append(j)
        ans += min_money

if ans <= k:
    print(ans)
else:
    print('Oh no')