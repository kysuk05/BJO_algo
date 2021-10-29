# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

from collections import deque


queue = deque()

n = input()
check = [0]*n

def()
while queue:
    x = queue.popleft()
    if x == 1:
        return(check[x])
    for i in range(3):
        if i == 0:
            if x%3 == 0:
                nx = x//3
                check[nx] = check[x]+1
