# 도시에는 N개의 빌딩이 있다.
# i번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
# i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, .... , N이다.
# 그런데 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.

# 첫 번째 줄에 빌딩의 개수 N이 입력된다.(1 ≤ N ≤ 80,000)
# 두 번째 줄 부터 N+1번째 줄까지 각 빌딩의 높이가 hi 입력된다. (1 ≤ hi ≤ 1,000,000,000)

# 2493번 후에 다음으로 풀게 된 스택문제.
# 마음에 들게 풀었다.

import sys
sta = []
ans = 0
a = int(sys.stdin.readline())
for i in range(a):
    b=int(sys.stdin.readline())
    while sta and sta[-1]<=b:
        sta.pop()
    ans += len(sta)
    sta.append(b)
print(ans)