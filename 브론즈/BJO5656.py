# C언어의 비교 연산자는 아래 표에 나와있다. 

# 연산자	뜻
# >	크다
# >=	크거나 같다
# <	작다
# <=	작거나 같다
# ==	같다
# !=	같지 않다
# 이 연산자는 두 피연산자를 비교하고, (왼쪽 값과 오른쪽 값) true또는 false (1 또는 0)을 리턴한다. 예를 들어, 2 > 3은 "false"를 리턴하고 (2는 3보다 작기 때문), 3 != 4는 "true", 3 >= 3은 "true"를 리턴한다.

# C언어의 비교 연산식이 주어졌을 때, 결과를 구하는 프로그램을 작성하시오.

import sys
n = 1
while True:
    s = sys.stdin.readline().split()
    res = ''
    if s[1] == 'E':
        break
    if s[1] == '>=':
        if int(s[0]) >= int(s[2]):
            res += 'True'
        else:
            res += 'False'
    elif s[1] == '>':
        if int(s[0]) > int(s[2]):
            res += 'True'
        else:
            res += 'False'
    if s[1] == '<=':
        if int(s[0]) <= int(s[2]):
            res += 'True'
        else:
            res += 'False'
    elif s[1] == '<':
        if int(s[0]) < int(s[2]):
            res += 'True'
        else:
            res += 'False'
    if s[1] == '==':
        if int(s[0]) == int(s[2]):
            res += 'True'
        else:
            res += 'False'
    if s[1] == '!=':
        if int(s[0]) != int(s[2]):
            res += 'True'
        else:
            res += 'False'
    
    print('Case '+str(n)+': '+res)
    n+=1