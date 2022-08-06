# 두 자연수 A, B가 주어졌을 때, A ≤ x ≤ B를 만족하는 모든 x에 대해 x를 이진수로 표현했을 때 1의 개수의 합을 구하는 프로그램을 작성하시오.

# 즉, f(x) = x를 이진수로 표현 했을 때 1의 개수라고 정의하고, 아래 식의 결과를 구하자.


n,m = map(int,input().split())

ans = 0




temp = bin(m)[2:]
dp = [0]
for i in range(len(temp)):
    dp.append(sum(dp)+2**i)
sp = [0]
for i in range(1,len(dp)):
    sp.append(sp[-1]+dp[i])

b = 0

while len(temp) != 0:
    if temp[0] == '1':
        b += sp[len(temp)-1]
        b += int(temp[0:],2)-2**len(temp[1:])+1
    temp = temp[1:]


a = 0
temp = bin(n-1)[2:]
while len(temp) != 0:
    if temp[0] == '1':
        a += sp[len(temp)-1]
        a += int(temp[0:],2)-2**len(temp[1:])+1
    temp = temp[1:]
print(b-a)