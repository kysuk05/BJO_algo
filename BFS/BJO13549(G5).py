# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.


from collections import deque


n,k = map(int,input().split())
queue = deque()
queue.append(n)

dx = [1,-1]
check = [0]*200001

check[n] = 1

def bfs():
    while queue:
        x = queue.popleft()
        if x < k and x >= 1:
            num = x
            while num < k:
                queue.append(num*2)
                check[num*2] = check[x]
                num = num*2
                if num == k:
                    return(check[x])
        if x == k:
            return(check[x])
        else:
            if x > k:
                nx = x-1
                if check[nx] != 0:
                    continue
                else:
                    check[nx] = check[x]+1
                    queue.append((nx))
            elif x < k:
                for i in range(2):
                    nx = x + dx[i]
                    if check[nx] != 0:
                        continue
                    else:
                        if x < 0:
                            continue
                        else:
                            check[nx] = check[x]+1
                            queue.append((nx))


print(bfs()-1)

        


