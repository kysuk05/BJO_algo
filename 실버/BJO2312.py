# 양의 정수 N이 주어졌을 때, 이 수를 소인수분해 한 결과를 출력하는 프로그램을 작성하시오.

import sys
from collections import Counter

n = int(sys.stdin.readline())



    
    
for i in range(n):
    li = []
    k = int(sys.stdin.readline())
    
    while True:
        num = 0
        for i in range(2,int(k**0.5)+1):
            if k%i == 0:
                num = 1
                li.append(i)
                k //= i
                break
        if num == 0:
            break
    if k != 1:
        li.append(k)
    for x,y in Counter(li).items():
        print(x,y)