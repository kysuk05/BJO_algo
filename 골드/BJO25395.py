# 정보통신기술(ICT)의 발달에 힘입어, 미래형 자동차로 여겨졌던 인터넷 연결을 통해 운전자에게 다양한 서비스를 제공하는 커넥티드 카(connected car)가 현실로 다가왔다. 현대오토에버는 이에 발맞춰 클라우드와 사물 인터넷을 비롯한 최신 ICT를 적용한 차세대 커넥티드 카 서비스 플랫폼을 구축하고, 최고의 커넥티드 카를 완성하기 위한 핵심 소프트웨어 기술을 축적하고 있다.

# 현대오토에버의 엔지니어 현오는 새로운 서비스를 생각하던 중, 커넥티드 카의 핵심 기술인 사물 인터넷과 위치 기반 기술을 접목한 실험을 해 보기로 했다. 현오가 개발한 실험용 프로그램은 다음과 같은 기능을 가지고 있다.

# 현오는 사물 인터넷에 연결된 커넥티드 카를 원격 조종할 수 있다.
# 사물 인터넷에 연결된 커넥티드 카가 그렇지 않은 커넥티드 카와 같은 위치에 있게 되면, 그 커넥티드 카를 사물 인터넷에 연결시킬 수 있다. 이후 두 커넥티드 카가 다시 서로 멀어지더라도 연결은 그대로 유지된다.
# 현오는 실험을 위해 $1$부터 $N$까지 번호가 매겨진 $N$대의 커넥티드 카를 일렬로 배치했다. $i$번 커넥티드 카의 초기 위치는 $x_i$이고, 연료량은 $h_i$이다. 모든 커넥티드 카는 $1$만큼의 연료를 소비해서 $1$의 거리만큼 이동할 수 있으며, 연료를 모두 소비하면 더 이상 움직일 수 없다.

# 처음에 커넥티드 카들은 모두 사물 인터넷에 연결되지 않은 상태이다. 현오는 먼저 $S$번 커넥티드 카를 사물 인터넷에 연결시키고, 프로그램의 기능을 적절히 사용해 다른 커넥티드 카들에 사물 인터넷을 전파하려고 한다.

# 현오가 커넥티드 카들을 어떻게 다루느냐에 따라 실험에서 사물 인터넷에 연결되는 커넥티드 카들의 조합은 달라질 수 있다. 현오가 다양한 방법으로 여러 번 실험을 진행할 때, 사물 인터넷에 연결될 가능성이 있는 커넥티드 카를 전부 구해 보자.


import sys

n,s = map(int,sys.stdin.readline().split())


con = list(map(int,sys.stdin.readline().split()))
feu = list(map(int,sys.stdin.readline().split()))

ans = []

x = s-1

st = x-1
en = x+1

ans.append(s)

le = con[x]-feu[x]

ri = con[x]+feu[x]

while st >= 0 and en < n and (le <= con[st] or ri >= con[en]):
    if le <= con[st]:
        ans.append(st+1)
        le = min(le,con[st]-feu[st])
        ri = max(ri,con[st]+feu[st])
        st -=1
    else:
        ans.append(en+1)
        le = min(le,con[en]-feu[en])
        ri = max(ri,con[en]+feu[en])
        en += 1

if st < 0:
    while en < n and ri >= con[en]:
        ans.append(en+1)
        ri = max(ri,con[en]+feu[en])
        en += 1
elif en >= n:
    while st >= 0 and le <= con[st]:
        ans.append(st+1)
        le = min(le,con[st]-feu[st])
        st -=1
ans.sort()
print(*ans)