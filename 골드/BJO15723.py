# 모든 중앙대 컴퓨터공학부(소프트웨어학부) 학생들은 미인이다.
# 지무근은 중앙대 컴퓨터공학부 학생이다.
# 그러므로 지무근은 미인이다.

# 위 연역 논증은 대표적인 삼단논법의 예시이다. 삼단논법이란 전제 두 개와 결론 하나로 이루어진 연역 논증이다. 이것을 응용하면, n개의 전제가 있을 때 m개의 결론을 도출할 수 있을 것이다. 이때의 n과 m은 모든 의미에서 적절한 수라고 가정하자. 자세한 것은 입출력 예시를 확인하자.

# 입력
# 첫째 줄에 정수 n(2 ≤ n ≤ 26)이 주어진다.

# 둘째 줄부터 n개의 줄에 걸쳐 각 줄에 전제가 하나씩 주어진다. 전제는 모두 a is b의 형식으로 주어지며 a와 b는 서로 다른 임의의 알파벳 소문자이다. 특별한 명시는 없지만 모든 전제는 “모든 a는 b이다”라는 의미이다. 하지만 “모든 b는 a이다”의 의미는 될 수 없다. 또한 a는 b이면서 c일 수 없으나, a와 b가 동시에 c일 수는 있다.

# n + 2번째 줄에 정수 m(1 ≤ m ≤ 10)이 주어진다. 그 다음 m개의 줄에 걸쳐 각 줄에 하나의 결론이 전제와 같은 형식으로 주어진다.


import sys
from collections import deque

n = int(sys.stdin.readline())

alpa = {}

for i in range(n):
    x,I,y = sys.stdin.readline().split()
    if x in alpa:
        alpa[x].append(y)
    else:
        alpa[x] = [y]

n = int(sys.stdin.readline())



for i in range(n):
    x,I,y = sys.stdin.readline().split()
    qu = deque()
    check = {}
    ans = 'F'
    if x in alpa:
        for i in range(len(alpa[x])):
            check[alpa[x][i]] = 0
            qu.append(alpa[x][i])
    while qu:
        x = qu.popleft()
        if x == y:
            ans = 'T'
            break
        
        if x in alpa:
            for i in range(len(alpa[x])):
                if alpa[x][i] not in check:
                    check[alpa[x][i]] = 0
                    qu.append(alpa[x][i])
    print(ans)