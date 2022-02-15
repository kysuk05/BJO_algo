# N개의 정수로 이루어진 수열 a1, ... , aN이 있다. 택희는 해당 수열이 증가수열 혹은 감소수열이 되게 만들고 싶다.

# 증가수열은 모든 i(1 ≤ i < N)에 대해서 ai ≤ ai+1을 만족하는 수열이고, 감소수열은 ai ≥ ai+1을 만족하는 수열이다.

# 택희는 해당 수열의 맨 앞의 k개의 원소를 맨 뒤로 옮겨서 증가수열 또는 감소수열을 만들고 싶다. 즉, ak+1, ..., aN, a1, ..., ak가 증가수열, 또는 감소수열이 돼야 한다. 옮기지 않는 경우는 k=0이라고 하자. 이때, 적절한 k를 골라서 원하는 수열을 만들 수 있게 도와줘라.


import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

check = 1000000001

if li[0] >= li[-1]:
    for i in range(1,n):
        if li[i] < li[i-1]:
            if check == 1000000001:
                check = i
            else:
                check = -1

check2 = 1000000001
if li[0] <= li[-1]:
    for i in range(1,n):
        if li[i] > li[i-1]:
            if check2 == 1000000001:
                check2 = i
            else:
                check2 = -1

if check != -1 and check2 != -1:
    check = min(check2,check)
elif check2 != -1:
    check = check2
if check == 1000000001:
    check = -1

t = 0
s = 0
for i in range(1,n):
    if li[i] > li[i-1]:
        t += 1
    elif li[i] < li[i-1]:
        s += 1
if t == 0 or s == 0:
    check = 0

print(check)