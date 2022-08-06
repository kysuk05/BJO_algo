import sys

n = int(sys.stdin.readline())

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


for i in prime:
    ans = {}
    temp = i
    ans[temp] = 0
    while True:
        if temp == 1:
            print(i)
            break
        temp = str(temp)
        sq = 0
        for j in temp:
            sq += int(j)**2
        temp = sq
        if temp in ans:
            break
        ans[temp] = 0