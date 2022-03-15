# 최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

# 최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.



import sys
from collections import deque

t = int(sys.stdin.readline())
inf = sys.maxsize

for _ in range(t):
    n,d,c = map(int,sys.stdin.readline().split())
    li = [[]for i in range(n+1)]
    check = [inf]*(n+1)
    qu = deque()
    check[c] = 1
    qu.append(c)
    
    for i in range(d):
        a,b,s = map(int,sys.stdin.readline().split())
        li[b].append((a,s))
    
    while qu:
        a = qu.popleft()
        for da,ds in li[a]:
            if check[da] > check[a] + ds:
                check[da] = check[a] + ds
                qu.append(da)
    
    
    check = [i for i in check if i != inf]
    print(len(check),max(check)-1)