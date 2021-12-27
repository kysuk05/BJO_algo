# 상근이는 은행에 가서 통장을 만들고 N원을 저금했다. 상근이는 이 통장에 입금이나 출금을 하지 않았다.

# 은행은 통장을 만든지 1년이 지날때마다 상근이의 통장에 저금되어 있는 돈의 B%만큼을 이자로 적립해준다.

# 상근이는 몇 년이 지나면 통장에 저금되어 있는 돈이 M원을 넘을지 궁금해졌다. 

# N,M,B가 주어졌을 때, 몇 년이 지나야 하는지 구하는 프로그램을 작성하시오.

import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == '':
        break
    a,b,c = map(float,n.split())
    an = 0
    while a <=c:
        a = a*(1+b/100)
        an += 1
    print(an)