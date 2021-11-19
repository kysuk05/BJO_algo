# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.


# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

import sys
n,m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


stack1 = []
stack2 = []

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            stack1.append((a,b))
        elif graph[a][b] == 2:
            stack2.append((a,b))
st = []
check = [0]*(len(stack2)+2)
index = [-1]


ans = 100000
def func(k):
    global index,ans
    if k == m:
        an = []
        for a in range(len(stack1)):
            mid = []
            for b in range(len(st)):
                x = stack1[a][0]-st[b][0]
                y = stack1[a][1]-st[b][1]
                if x < 0:
                    x = -x
                if y < 0:
                    y = -y
                mid.append(x+y)
            an.append(min(mid))
        if sum(an) < ans:
            ans = sum(an)
        
    else:
        for i in range(len(stack2)):
            if check[i] == 0 and index[-1] < i:
                index.append(i)
                st.append(stack2[i])
                func(k+1)
                index.pop()
                st.pop()

func(0)
print(ans)