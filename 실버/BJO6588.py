n = 1000000

graph = [0]*(n+1)
prime = [0]*(n+1)
for i in range(2,n+1):
    if graph[i] == 0:
        prime[i] = 1
    an = i
    graph[an] = 1
    an = an**2
    while an < n+1:
        graph[an] = 1
        an+=i


while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(n,-1,-1):
        if prime[i] == 1 and prime[n-i] == 1:
            print(str(n)+' = '+str(n-i)+' + '+str(i))
            break