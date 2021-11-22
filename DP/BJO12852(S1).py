# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

import sys
n = int(input())
stack = [0]*(n+1)
pre = [0]*(n+1)
for i in range(2,n+1):
    stack[i] = stack[i-1]+1
    pre[i] = i-1
    if i%2 == 0:
        if stack[i//2] +1 < stack[i]:
            stack[i] = stack[i//2]+1
            pre[i] = i // 2
    if i%3 == 0:
        if stack[i//3] +1 < stack[i]:
            stack[i] = stack[i//3]+1
            pre[i] = i // 3

print(stack[n])


num = n

print(num,end=' ')
while num != 1:
    print(pre[num],end=' ')
    num = pre[num]