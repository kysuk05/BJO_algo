# L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.


import sys


a,b = sys.stdin.readline().split()

ans = 0
if len(a) != len(b):
    print(ans)
else:
    for i in range(len(a)):
        if a[i] == b[i] and a[i] == '8':
            ans +=1
        elif a[i] != b[i]:
            break
    print(ans)