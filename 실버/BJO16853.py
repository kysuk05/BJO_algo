#정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

#2를 곱한다.
#1을 수의 가장 오른쪽에 추가한다. 
#A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

#입력
#첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.


from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())

queue = deque()
queue.append((m,1))
find = 0
while queue:
    num,check = queue.popleft()
    if num == n:
        print(check)
        find = 1
        break
    if num < n:
        continue
    
    if num % 10 == 1:
        queue.append((num//10,check+1))
    if num % 2 == 0:
        queue.append((num//2,check+1))

if find == 0:
    print(-1)