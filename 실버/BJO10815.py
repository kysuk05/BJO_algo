# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.


import sys

n = int(sys.stdin.readline())

se = set(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

for i in arr:
    if i in se:
        print(1,end=' ')
    else:
        print(0,end=' ')