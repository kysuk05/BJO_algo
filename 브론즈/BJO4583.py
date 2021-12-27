# 소문자 b와 d나 p와 q는 서로 거울상 관계이다. 또한 i,o,v,w와 x는 모두 자신과 거울상 관계이다. 이 외에도 몇 가지 거울상 관계인 문자들이 존재하지만, 이 문제에서는 위에서 언급한 문자들만 거울상 관계로 생각하도록 하자.

# 이러한 대칭성으로 인해 위의 문자들로 이루어진 단어들은 거울에 비친 모습을 보고 거울에 반사되기 전 모습을 유추하는 것이 가능하다. 예를들어, 'boxwood'는 반사되기 전 'boowxod', 'ibid'는 반사되기 전 'bidi'라는 단어일 것이다. 몇 단어들이 주어질 때, 거울에 비춰지기 전 모습을 표현할수 있는지 판단하여라.

import sys

while True:
    t = sys.stdin.readline().rstrip()
    if t == '#':
        break
    li = []
    check = 0
    for i in t:
        if i in ('i','o','v','w','x'):
            li.append(i)
        elif i == 'b':
            li.append('d')
        elif i == 'd':
            li.append('b')
        elif i == 'p':
            li.append('q')
        elif i == 'q':
            li.append('p')
        else:
            check = 1
    if check == 0:
        li.reverse()
        print(''.join(li))
    else:
        print('INVALID')