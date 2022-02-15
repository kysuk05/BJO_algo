# 1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.

# 임의의 순열은 정렬을 할 수 있다. 예를 들어  N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다. 첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이….

# N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.

import sys
from collections import deque

n = int(sys.stdin.readline())

num_list = list(range(1,n+1))
Q = deque(list(map(int,sys.stdin.readline().split())))

def fac(n):
    t = 1
    while n >0:
        t*=n
        n-=1
    return t


question = Q.popleft()

if question == 1:
    num = (Q.popleft())-1
    ans_list = []
    while num_list:
        t = num_list.pop(num//fac(len(num_list)-1))
        num %= fac(len(num_list))
        ans_list.append(t)
    for i in ans_list:
        print(i,end=' ')
elif question == 2:
    index_lis = []
    while Q:
        num = Q.popleft()
        index_lis.append((num_list.index(num),len(num_list)))
        num_list.remove(num)
    ans = 1
    for x,y in index_lis:
        ans += x*fac(y-1)
    print(ans)