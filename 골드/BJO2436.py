# 어떤 두 자연수에 공통인 약수들 중에서 가장 큰 수를 최대공약수라고 하고, 두 자연수의 공통인 배수들 중에서 가장 작은 수를 최소공배수라고 한다. 

# 예를 들어, 두 자연수 12와 90의 최대공약수는 6이며, 최소공배수는 180이다.

# 이와 반대로 두 개의 자연수 A, B가 주어졌을 때, A를 최대공약수로, B를 최소공배수로 하는 두 개의 자연수를 구할 수 있다. 그러나, 이러한 두 개의 자연수 쌍은 여러 개 있을 수 있으며, 또한 없을 수도 있다. 

# 예를 들어, 최대공약수가 6이며 최소공배수가 180인 두 정수는 위의 예에서와 같이 12와 90일 수도 있으며, 30과 36, 18과 60, 혹은 6과 180일 수도 있다. 그러나, 최대공약수가 6이며 최소공배수가 20인 두 자연수는 있을 수 없다.

# 두 개의 자연수가 주어졌을 때, 이 두 수를 최대공약수와 최소공배수로 하는 두 개의 자연수를 구하는 프로그램을 작성하시오. 

from itertools import combinations
from collections import Counter

a,b = map(int,input().split())

num = a*b
temp_num = num

arr = []
while num != 1:
    div_num = 1
    while True:
        div_num += 1
        if num % div_num == 0:
            arr.append(div_num)
            num //= div_num
            break
if len(arr) == 1:
    arr.append(1)

sqrt_num = int((a*b)**0.5)


common = []
while a != 1:
    div_num = 1
    while True:
        div_num += 1
        if a % div_num == 0:
            common.append(div_num)
            a //= div_num
            break

ans = 1
while common:
    t = common.pop()
    for i in range(2):
        arr.remove(t)
    ans *= t

count_arr = Counter(arr)
arr = []
for x,y in count_arr.items():
    arr.append(x**y)

an = ans

for i in range(1,len(arr)):
    comb = list(combinations(arr,i))
    for j in range(len(comb)):
        temp = an
        for k in comb[j]:
            temp *= k
        if temp <= sqrt_num:
            ans = max(ans,temp)

print(ans,temp_num//ans)