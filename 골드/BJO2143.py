# 한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

# 예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

# T(=5) = A[1] + B[1] + B[2]
#       = A[1] + A[2] + B[1]
#       = A[2] + B[3]
#       = A[2] + A[3] + B[1]
#       = A[3] + B[1] + B[2]
#       = A[3] + A[4] + B[3]
#       = A[4] + B[2] 

import sys

T = int(sys.stdin.readline())

a = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

b = int(sys.stdin.readline())

B = list(map(int,sys.stdin.readline().split()))

sum_a = [0]
total = 0
for i in range(a):
    total+=A[i]
    sum_a.append(total)

sum_b = [0]
total = 0
for i in range(b):
    total+=B[i]
    sum_b.append(total)

ans = 0

dic_a = {}
dic_b = {}

for i in range(len(sum_a)):
    for j in range(i):
        if sum_a[i]-sum_a[j] in dic_a:
            dic_a[sum_a[i]-sum_a[j]] += 1
        else:
            dic_a[sum_a[i]-sum_a[j]] = 1

for i in range(len(sum_b)):
    for j in range(i):
        if sum_b[i]-sum_b[j] in dic_b:
            dic_b[sum_b[i]-sum_b[j]] += 1
        else:
            dic_b[sum_b[i]-sum_b[j]] = 1

for i in dic_a.keys():
    if T-i in dic_b:
        ans += dic_a[i]*dic_b[T-i]
print(ans)