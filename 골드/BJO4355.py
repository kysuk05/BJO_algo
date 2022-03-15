# 양의 정수 n이 주어졌을 때, n보다 작은 양의 정수 중에서 n과 서로소인 수 개수를 구하는 프로그램을 작성하시오.

# 두 정수 a와 b가 서로소가 되려면 x > 1, y > 0, z > 0이면서, a = xy, b= xz를 만족하는 정수가 없어야 한다.



import sys

def div(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            if i not in li:
                li.append(i)
            n //= i
            break
    return n


while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    li = []
    n = num
    while True:
        k = div(n)
        if k == n:
            if k not in li and k != num:
                li.append(k)
            break
        else:
            n = k
    if not li:
        print(num-1)
    else:
        for i in li:
            num = num//i*(i-1)
        print(num)