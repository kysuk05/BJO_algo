# 진영이는 캠프 조교를 온 후 효율적으로 시간 관리를 해야 한다는 것을 깨달았다. 진영이는 하루에 해야 할 일이 총 N개가 있고 이 일들을 편하게 1번부터 N번까지 차례대로 번호를 붙였다.

# 진영이는 시간을 효율적으로 관리하기 위해, 할 일들에 대해 끝내야할 시간과 걸리는 시간을 적은 명단을 만들었다. 즉, 이 명단은 i번째 일은 일을 처리하는데 정확히 Ti 시간이 걸리고 Si 시 내에 이 일을 처리하여야 한다는 것을 담고 있다. 진영이는 0시부터 활동을 시작할 수 있고, 두 개 이상의 일을 같은 시간에 처리할 수 없다.

# 진영이가 바라는 점은 최대한 늦잠을 자는 것이다. 문제는 이러한 진영이를 도와 일들은 모두 마감시간 내에 처리할 수 있는 범위 내에서 최대한 늦게 일을 시작할 수 있는 시간이 몇 시인지 알아내는 것이다.

import sys
n = int(sys.stdin.readline())

sch = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    
    sch.append((b,a))
sch.sort()


a,b = sch.pop()

t = a-b
while sch:
    x,y = sch.pop()
    if x > t:
        t -= y
    else:
        t = x
        t -= y

if t < 0:
    print(-1)
else:
    print(t)