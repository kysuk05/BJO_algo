# 당신은 루머를 믿는가?

# 한 유명 심리학 실험에서는 사람들에게 두 개의 줄을 보여주고, 어떤 줄이 더 긴지 말하라 했다. 사실 한 사람을 제외하고 나머지는 실험자에 의해 사전에 조작된 사람들이었다. 조작된 사람들은 사실상 더 짧은 줄을 더 길다고 말했다. 주변 모두가 같은 답변을 하자, 진짜 피실험자 또한 짧은 줄이 더 길다고 말했다. 이 실험은 사람들이 주변인의 영향을 강하게 받는다는 것을 보여주었는데, 루머도 이와 같다.

# 루머는 최초 유포자로부터 시작한다. 최초 유포자는 여러 명일 수 있고, 최초 유포자를 제외하고 스스로 루머를 만들어 믿는 사람은 없다.

# 매분 루머를 믿는 사람은 모든 주변인에게 루머를 동시에 퍼트리며, 군중 속 사람은 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿는다.

# 루머를 믿는 순간부터 다른 말은 듣지 않기 때문에, 한번 믿은 루머는 계속 믿는다.

# 이때, 사람들이 루머를 처음 믿기 시작하는 시간을 알아내 보자.


import sys
from collections import deque

n = int(sys.stdin.readline())

people = [[]]

for i in range(n):
    t = list(map(int,sys.stdin.readline().rstrip().rstrip('0').split()))
    people.append(t)


check = [0 for i in range(n+1)]


upo = int(sys.stdin.readline())
upo_arr = list(map(int,sys.stdin.readline().split()))

qu = deque()

for i in upo_arr:
    check[i] = 1
    qu.append(i)

def che():
    while qu:
        x = qu.popleft()
        for i in people[x]:
            if check[i] == 0:
                cnt = 0
                for j in people[i]:
                    if check[j] != 0:
                        cnt += 1
                if cnt >= len(people[i])//2+len(people[i])%2:
                    x_arr.append(i)
    return check[x]
x_arr = []
t = che()
while x_arr:
    for k in x_arr:
        check[k] = t+1
        qu.append(k)
    x_arr = []
    t = che()
                

for i in range(1,len(check)):
    print(check[i]-1,end=' ')