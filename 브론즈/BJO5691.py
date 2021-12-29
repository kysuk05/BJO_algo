# 세 정수 A, B, C의 평균은 (A+B+C)/3이다. 세 정수의 중앙값은 수의 크기가 증가하는 순서로 정렬했을 때, 가운데 있는 값이다.

# 두 정수 A와 B가 주어진다. 이때, A, B, C의 평균과 중앙값을 같게 만드는 가장 작은 정수 C를 찾는 프로그램을 작성하시오.

import sys
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        n1 = max(a,b)
        n2 = min(a,b)
        print(n2-(n1-n2))