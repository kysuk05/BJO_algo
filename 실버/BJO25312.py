# 음료수가 담긴 병이 총 $N$개 있다. $i$번째 병에는 음료수가 총 $w_i$ ℓ만큼 담겨있고, 음료수에는 설탕이 총 $v_i$ mg만큼 들어 있다. 이 음료수들 중 일부를 섞어서 총용량이 정확히 $M$ ℓ인 혼합 음료수를 만들려고 한다. 이때, 병에 있는 음료수를 일부만 사용해도 된다.

# 혼합 음료수의 설탕량은 섞은 음료수들 각각에 들어 있는 설탕량의 합으로 결정된다. 설탕은 음료수에 균일하게 녹아 있기 때문에, 어떤 병에 든 음료수를 일부만 사용할 경우 설탕 역시 그 비율만큼 들어가게 된다. 즉, $i$번째 음료수를 $a_i$ ℓ만큼$(0 \le a_i \le w_i)$ 섞는다면, $i$번째 음료수에 해당하는 설탕량은 
 
# $\left(\frac{a_i}{w_i} \times v_i\right)$ mg이다.

# 음료수를 섞어 총용량이 정확히 $M$ ℓ인 혼합 음료수를 만들었을 때, 여기에 들어갈 수 있는 설탕량의 최댓값을 출력하여라.

import sys

N,M = map(int,sys.stdin.readline().split())

sugar = []

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    c = b/a
    sugar.append((c,a,b))

sugar.sort()


mix = 0
su = 0
while True:
    if mix + sugar[-1][1] >= M:
        break
    mix += sugar[-1][1]
    su += sugar[-1][2]
    sugar.pop()

a,b,c = sugar[-1]

c *= M-mix

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)
    
d = gcd(c,b)

b //= d
c //= d

c += su*b

print(str(c)+'/'+str(b))