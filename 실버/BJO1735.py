# 분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.

# 두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.


a,b = map(int,input().split())
c,d = map(int,input().split())


def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

n = gcd(b,d)

num = (b//n)*(d//n)*n

num2 = a*(num//b)+c*(num//d)


gcd_num = gcd(num2,num)

print(num2//gcd_num,num//gcd_num)