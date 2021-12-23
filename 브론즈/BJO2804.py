# 창영이는 크로스워드 퍼즐을 만들려고 한다.

# 두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다) 공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.

# .C..
# .C..
# ABBA
# .B..
# 입력
# 첫째 줄에 두 단어 A와 B가 주어진다. 두 단어는 30글자 이내이고, 공백으로 구분되어져 있다. 또, 대문자로만 이루어져 있고, 적어도 한 글자는 두 단어에 포함되어 있다.


s,t = map(str,input().split())

graph = [['.'for i in range(len(s))]for j in range(len(t))]
check = 0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            check = 1
            an1 = i
            an2 = j
            break
    if check == 1:
        break

for a in range(len(s)):
    graph[an2][a] = s[a]
for b in range(len(t)):
    graph[b][an1] = t[b]

for i in range(len(graph)):
    print(''.join(graph[i]))
