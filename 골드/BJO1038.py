# 음이 아닌 정수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소할 때, 그 수를 줄어드는 수라고 한다. 예를 들어, 321와 950은 줄어드는 수이고, 322와 958은 아니다.

# N번째로 작은 줄어드는 수를 출력하는 프로그램을 작성하시오. 만약 그러한 수가 없을 때는 -1을 출력한다. 가장 작은 줄어드는 수가 1번째 작은 줄어드는 수이다.

from collections import deque

cnt = int(input())

num = deque(['0','1','2','3','4','5','6','7','8','9'])

total = -1

while num:
    x = num.popleft()
    total +=1
    if total == cnt:
        print(x)
        cnt = 0
        break
    for i in range(10):
        if int(x[-1])>i:
            num.append(x+str(i))

if cnt != 0:
    print(-1)