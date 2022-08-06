# 상근이는 Sogang ACM-ICPC Team의 회장이다. 서강대학교 컴퓨터 학생들은 하나 또는 그 이상의 학회에 소속되어 있다. 상근이는 학생들이 어떤 학회에 소속되어 있는지 조사해보려고 한다.

# 상근이는 학회원의 정보를 다음과 같이 작성한다. 아래 예시는 sisobus와 weissblume은 icpc의 학회원이라는 뜻이다.

# icpc:weissblume,sisobus.
# 콜론(:)의 앞에는 학회의 이름이 쓰여 있고, 뒤에는 학회원이 주어진다.

# 어떤 학회는 모든 회원이 다른 학회에 소속되어 있을 수도 잇다. 따라서, 학회원을 적는 곳에 학회의 이름을 적을 수도 있다.

# slug:sisobus,minhyeok,icpc,exupery.
# icpc에 소속되어 있는 사람은 slug에도 소속되어 있다는 뜻이다. 즉, slug의 학회원은 아래와 같다.

# slug:sisobus,minhyeok,weissblume,sisobus,exupery.
# 이 경우에 sisobus는 두 번 등장한다. 중복되는 사람의 이름을 하나로 줄이게 되면, 아래와 같이 하나로 줄여서 작성할 수 있다.

# slug:sisobus,minhyeok,weissblume,exupery.
# 학회의 회원 정보가 주어졌을 때, 각 학회의 학회원이 몇 명인지 구하는 프로그램을 작성하시오.

# 상근이가 작성하는 방법에는 학회의 이름이 중첩될 수도 있다. 아래 예시에서 one에 소속된 회원은 abckhw 한 명이다.

# one:another.
# another:yetanother.
# yetanother:abckhw.


import sys
from collections import deque

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    dic = {}
    
    qu = deque()
    
    for i in range(n):
        a,b = sys.stdin.readline().rstrip().split(':')
        
        person = b[:-1].split(',')
        dic[a] = person
        if i == 0:
            for j in person:
                qu.append(j)
    
    ans = set()
    group = {}
    while qu:
        x = qu.popleft()
        if x in dic:
            for i in dic[x]:
                if i not in group:
                    qu.append(i)
                    group[i] = 0
        else:
            ans.add(x)
    print(len(ans))

    
    