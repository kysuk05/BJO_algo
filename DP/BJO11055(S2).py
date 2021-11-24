# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)


import sys

n = int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split()))

sum = [graph[0]]
for i in range(1,len(graph)):
    check = 0
    stack = []
    for j in range(i-1,-1,-1):
        if graph[j] < graph[i]:
            stack.append(j)
            check = 1
    if check == 0:
        sum.append(graph[i])
    else:
        num = stack[0]
        for k in stack:
            if sum[k] > sum[num]:
                num = k
        sum.append(sum[num]+graph[i])

print(max(sum))