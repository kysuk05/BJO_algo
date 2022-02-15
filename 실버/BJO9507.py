# 꿍은 군대에서 진짜 할짓이 없다. 그래서 꿍만의 피보나치를 만들어보려고 한다. 기존의 피보나치는 너무 단순해서 꿍은 좀더 복잡한 피보나치를 만들어보고자 한다. 그래서 다음과 같은 피보나치를 만들었다. 꿍만의 피보나치 함수가 koong(n)이라고 할 때,

# n < 2 :                         1
# n = 2 :                         2
# n = 3 :                         4
# n > 3 : koong(n − 1) + koong(n − 2) + koong(n − 3) + koong(n − 4)
# 이다.

# 여러분도 꿍 피보나치를 구해보아라.


import sys

n = int(sys.stdin.readline())

koong = [1,1,2,4]

for i in range(n):
    t = int(sys.stdin.readline())
    if t+1 < len(koong):
        print(koong[t])
    else:
        for i in range(t-len(koong)+1):
            koong.append(koong[-1]+koong[-2]+koong[-3]+koong[-4])
        print(koong[t])