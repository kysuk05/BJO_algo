# 1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면  
#  \(\begin{pmatrix} 1 & 2 &3&4&5&6&7&8 \\  3& 2&7&8&1&4&5&6 \end{pmatrix}\) 와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.

# 순열을 배열을 이용해  
#  \(\begin{pmatrix} 1 & \dots & i & \dots &n \\  \pi_1& \dots& \pi_i & \dots & \pi_n \end{pmatrix}\) 로 나타냈다면, i에서 πi로 간선을 이어 그래프로 만들 수 있다.

# Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.

# N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.



import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))
    
    qu = deque()
    check = [0]*(t+1)
    ans = 0
    for i in range(t):
        if check[i] == 0:
            check[i] == 1
            qu.append(li[i]-1)
            while qu:
                x = qu.popleft()
                if check[x] == 0:
                    check[x] = 1
                    qu.append(li[x]-1)
            ans += 1
    print(ans)