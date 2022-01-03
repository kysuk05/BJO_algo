# n!은 정수 n에 대한 팩토리얼 수를 나타내는데, 이는 1부터 n까지의 모든 정수의 곱을 의미한다. 팩토리얼은 굉장히 빨리 커지기 때문에 13!는 대부분의 컴퓨터에서 32비트 정수형을, 70!은 대부분의 부동 소수점 변수의 범위를 넘어선다. 우리는 n!에 대하여 0이 아닌 최우측 수(the rightmost non-zero digit)를 찾으려고 한다. 예를 들어, 5! = 1 * 2 * 3 * 4 * 5 = 120 이므로 5!의 최우측 0이 아닌 수는 2이다. 마찬가지로 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040이며 7!의 0이 아닌 최우측 수는 4가 된다.



import sys

n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    su = 1
    for j in range(1,t+1):
        su *= j
    li = []
    for k in str(su):
        li.append(k)
    while li:
        a = li.pop()
        if a != '0':
            print(a)
            break