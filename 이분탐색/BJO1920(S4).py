# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.


import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

li.sort()

st = 0
en = n-1

t = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))

for j in range(t):
    an = lis[j]
    st = 0
    en = n-1
    while True:
        num = (st+en)//2
        if an == li[num]:
            print(1)
            break
        if en-st == 0:
            print(0)
            break
        else:
            if an > li[num]:
                st = num+1
            elif an < li[num]:
                en = num