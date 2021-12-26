# 만약 단어 A의 알파벳 순서를 바꿔서 단어 B를 만들 수 있다면, 두 단어는 애너그램이라고 한다. 예를 들어, occurs는 succor의 애너그램이지만, dear는 dared의 애너그램이 아니다. 영어에서 가장 유명한 애너그램은 dog와 god이다.

# 두 단어의 애너그램 거리란, 두 단어가 애너그램이 되기 위해서 지워야하는 단어의 최소 개수이다. 예를 들어, sleep과 leap이 주어졌다면, sleep에서 2개, leap에서 1개를 지운다면 두 단어는 애너그램 관계가 된다. 따라서, sleep과 leap의 애너그램 거리는 3이다. 서로 공통된 알파벳이 없는 dog와 cat같은 경우에는 모든 단어를 지워야 하기 때문에, 애너그램 거리가 6이다.

# 두 단어가 주어졌을 때, 두 단어의 애너그램 거리를 구하는 프로그램을 작성하시오.


import sys

n = int(sys.stdin.readline())

for i in range(n):
    di = {}
    dic = {}
    a = sys.stdin.readline().rstrip()
    for j in a:
        if j in di:
            di[j] += 1
        else:
            di[j] = 1
    b = sys.stdin.readline().rstrip()
    for j in b:
        if j in di:
            di[j] -= 1
            if di[j] == 0:
                di.pop(j)
        else:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
    print('Case #'+str(i+1)+':',sum(di.values())+sum(dic.values()))