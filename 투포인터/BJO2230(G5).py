# N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

# 예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.

# 일반적인 방법 : 메모리 초과
# import sys
# from itertools import combinations
# n,m = map(int,sys.stdin.readline().split())
# li = []
# for i in range(n):
#     li.append(int(sys.stdin.readline()))

# k = list(combinations(li,2))
# su = []
# for j in range(len(k)):
#     x,y = k[j][0],k[j][1]
#     if abs(x-y) >= m:
#         su.append(abs(x-y))
# print(min(su))

#투포인터를 이용한 방법
import sys
n,m = map(int,sys.stdin.readline().split())

li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()

sum = 10**20
end = 0
for j in range(n):
    while end < n:
        if li[end]-li[j] < m:
            end += 1
        elif sum > li[end]-li[j]:
            sum = li[end]-li[j]
            break
        else:
            break
print(sum)
