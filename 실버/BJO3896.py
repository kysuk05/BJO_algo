# 연속한 소수 p와 p+n이 있을 때, 그 사이에 있는 n-1개의 합성수(소수나 1이 아닌 양의 정수)는 길이가 n인 소수 사이 수열라고 부른다.

# 양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이를 구하는 프로그램을 작성하시오. k를 포함하는 소수 사이 수열이 없을 때는 길이가 0이다.

# 예를 들어, 소수 23과 29의 소수 사이 수열은 {24, 25, 26, 27, 28}이고, 길이는 6이다.

import sys

n = 1299709

graph = [0]*(n+1)
prime = []
for i in range(2,n+1):
    if graph[i] == 0:
        prime.append(i)
    an = i
    an = an**2
    while an < n+1:
        graph[an] = 1
        an+=i



T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    if graph[k] == 0:
        print(0)
    else:
        for j in range(1,len(prime)):
            if prime[j] > k and prime[j-1] < k:
                print(prime[j]-prime[j-1])
        