# 방탈출 게임을 하던 혜민이는 마지막 문제에 봉착했다. 단서는 다음과 같다.

# 앞에는 일렬로 놓여진 N개의 버튼이 모두 불이 꺼진 상태로 있다.
# 0 또는 1로 구성되어 있는 N자리 수가 적힌 쪽지가 있다.
# 0은 불이 꺼진 버튼, 1은 불이 켜진 버튼을 뜻한다.
# 불이 켜져 있는 버튼을 누르면 불이 꺼지고, 불이 꺼져 있는 버튼을 누르면 불이 켜진다.
# 버튼을 누르면 그 버튼 뿐만이 아닌 오른쪽 두 개의 버튼도 같이 눌린다. 
# 혜민이는 현재 모두 불이 꺼진 상태에서 버튼을 최소로 눌러서 쪽지와 똑같은 상태로 만들어야 한다는 것을 알아냈다! 혜민이를 도와줘서 방탈출 게임에 성공하자.


import sys

n = int(sys.stdin.readline())
button = list(map(int,sys.stdin.readline().split()))


now = [0 for i in range(n)]

ans = 0

for i in range(n):
    if now[i] != button[i]:
        ans += 1
        if i+1 < n:
            if now[i+1] == 1:
                now[i+1] = 0
            else:
                now[i+1] = 1
        if i+2 < n:
            if now[i+2] == 1:
                now[i+2] = 0
            else:
                now[i+2] = 1

print(ans)