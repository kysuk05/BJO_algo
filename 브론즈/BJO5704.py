# 팬그램은 알파벳의 모든 글자들을 사용해서 만든 문장이다. "the quick brown fox jumps over a lazy dog"과 "jackdaws loves my big sphinx of quartz"은 팬그램이다. 문장이 주어졌을 때, 팬그램인지 아닌지를 알아내는 프로그램을 작성하시오.

import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '*':
        break
    else:
        di = {}
        for i in range(1,27):
            di[i] = 0
        for i in s:
            if i != ' ' and ord(i)-96 in di:
                di.pop(ord(i)-96)
        if di:
            print('N')
        else:
            print('Y')