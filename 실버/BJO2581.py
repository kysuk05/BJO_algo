# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

m = int(input())
n = int(input())

graph = [0]*(n+1)
prime = []
graph[0] = 1
graph[1] = 1
for i in range(2,int(n**(1/2))+1):
    cnt = 2
    while cnt*i <= n:
        if graph[i*cnt] == 0:
            graph[i*cnt] = 1
        cnt += 1

lis = graph[m:n+1]

for j in range(len(lis)):
    if lis[j] == 0:
        prime.append(j+m)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)