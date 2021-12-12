# 정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다. 정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.

# 입력
# 첫 번째 줄에는 총 입력 받을 걸그룹의 수 N(0 < N < 100)과 맞혀야 할 문제의 수 M(0 < M < 100)을 입력받는다.

# 두 번째 줄부터는 각 걸그룹마다 팀의 이름, 걸그룹의 인원 수, 멤버의 이름을 한 줄씩 차례대로 입력받는다. 팀과 멤버의 이름은 최대 100글자이며, 모든 글자는 알파벳 소문자이다. 하나의 걸그룹이나 서로 다른 두 걸그룹에 이름이 같은 두 멤버가 있는 경우는 없다.

# 그 다음 줄부터는 M개의 퀴즈를 입력받는다. 각각의 퀴즈는 두 줄로 이루어져 있으며, 팀의 이름이나 멤버의 이름이 첫 줄에 주어지고 퀴즈의 종류를 나타내는 0 또는 1이 두 번째 줄에 주어진다. 퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름이 주어진다.


import sys
n,m = map(int,sys.stdin.readline().split())

di = {}
for i in range(n):
    li = []
    gr = sys.stdin.readline().rstrip()
    nu = int(sys.stdin.readline())
    for j in range(nu):
        li.append(sys.stdin.readline().rstrip())
    li.sort()
    for k in range(len(li)):
        di[li[k]] = gr

for a in range(m):
    na = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline())
    if q:
        print(di[na])
    else:
        for ke,val in di.items():
            if val == na:
                print(ke)