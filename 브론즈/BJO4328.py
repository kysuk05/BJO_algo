# 음이 아닌 b진법 정수 p와 m이 주어졌을 때, p를 m으로 나눈 나머지를 b진법으로 구하는 프로그램을 작성하시오.

# p를 m으로 나눈 나머지란 임의의 정수 a에 대해서 p = a*m + k를 만족하는 가장 작은 k를 말한다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 3개의 정수가 한 줄로 이루어져 있다. 첫 번째 숫자는 b이고, 2보다 크거나 같고, 10보다 작거나 같은 값을 가진다. 두 번째 숫자는 p이고, 세 번째 숫자는 m이다. p와 m은 0과 b-1사이의 수로만 이루어져 있고, p의 최대 길이는 1000, m의 최대 길이는 9이다.

# 마지막 줄에는 0이 하나 주어진다.

import sys
while True:
    t = sys.stdin.readline().rstrip()
    if t == '0':
        break
    else:
        b,p,m = map(str,t.split())
        b = int(b)
        p = int(p,b)
        m = int(m,b)
        an = p%m
        li = []
        if an == 0:
            li.append('0')
        else:
            while an != 0:
                li.append(str(an%b))
                an //= b
        li.reverse()
        print(''.join(li))
        