# 대전 ACM-ICPC Regional가 끝나면, 대회 참가자들은 다같이 카이스트 근처의 동혁 피자에 간다. 대회는 5시간동안 진행되므로, 참가자는 모두 배가 매우 고프다. 피자를 최대한 빨리 먹기 위해서, 큰 피자를 하나 시키려고 한다. 생각해보니 피자가 너무 크면 식탁 위에 맞지 않을 수도 있다. 식탁은 원이고, 피자는 직사각형이다. 식탁의 반지름과 피자의 크기가 주어졌을 때, 피자가 식탁에 맞는 크기인지 아닌지를 구하는 프로그램을 작성하시오.

import sys
t = 0
while True:
    t += 1
    s = sys.stdin.readline().split()
    if s[0] == '0':
        break
    if (int(s[0])*2)**2 >= int(s[1])**2+int(s[2])**2:
        print('Pizza '+str(t)+' fits on the table.')
    else:
        print('Pizza '+str(t)+' does not fit on the table.')