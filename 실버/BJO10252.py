# m × n 직사각 그리드(rectangular grid)는, x-좌표의 범위가 0부터 n-1까지인 정수이고 y-좌표의 범위가 0부터 m-1까지 정수인 평면상의 점들에 대응하는 정점들을 가지고, 두 정점에 대응하는 두 점 사이의 거리가 1 일 때에만 그 둘을 잇는 에지가 있는 그래프다. 예를 들어, 4 × 6 직사각 그리드가 그림 1 에 있다. 이 그리드는 m개 행 각각에 n개의 정점이 있고, n개 열 각각에 m 개의 정점이 있다. 행 i와 열 j에 있는 정점을 (i,j)라고 나타낸다. 여기서 0 ≤ i ≤ m-1이고 0 ≤ j ≤ n-1이다.

# m × n 직사각 그리드의 모든 행 i ∈ {0, … , m-1}에 대하여 두 정점 (i, 0)과 (i, n-1)을 잇는 에지를 추가하고, 또한 모든 열 j ∈ {0, … , n-1} 에 대하여 두 정점 (0, j) 와 (m-1, j) 을 잇는 에지를 추가하면, 그림 2 에 보인 것과 같이 각 행은 길이 n인 사이클을 이루고 각 열은 길이 m인 사이클을 이루게 된다. 이렇게 만들어진 그래프를 종종 m × n 토로이드 그리드(toroidal grid) 라고 부르는데, 왜냐하면 이 그래프를 토러스(torus)에 에지가 교차하지 않도록 그릴 수 있기 때문이다.



# 주어진 m × n 토로이드 그리드에 대하여, 모든 정점을 정확히 한번씩 지나는 사이클을 찾는 프로그램을 작성하시오. 문제에서 요구하는 사이클은 그래프에 있는 서로 다른 mn개 정점들의 열 (v1, v2, … , vmn)로 나타낼 수 있는데, 이때 모든 k ∈ {1, … , mn-1}에 대하여 vk와 vk+1은 인접하며 또한 vmn과 v1도 인접하여야 한다.



def down(a,b):
    print('('+str(a)+','+str(b)+')')
    return (a+1,b)
def up(a,b):
    print('('+str(a)+','+str(b)+')')
    return (a-1,b)
def left(a,b):
    print('('+str(a)+','+str(b)+')')
    return (a,b-1)
def right(a,b):
    print('('+str(a)+','+str(b)+')')
    return (a,b+1)



import sys

t = int(sys.stdin.readline())

for i in range(t):
    m,n = map(int,sys.stdin.readline().split())
    a = 0
    b = 0
    print(1)
    if m%2 == 0:
        for _ in range(m-1):
            a,b = down(a,b)
        a,b = right(a,b)
        for i in range(m):
            for _ in range(n-2):
                a,b = right(a,b)
            a,b = up(a,b)
            for _ in range(n-2):
                a,b = left(a,b)
                if a == 0 and b == 1:
                    print('('+str(a)+','+str(b)+')')
                    break
            if a == 0 and b == 1:
                    break
            a,b = up(a,b)
    
    else:
        for _ in range(m-1):
            a,b = down(a,b)
        a,b = right(a,b)
        for i in range(m):
            for _ in range(n-2):
                a,b = right(a,b)
                if a == 0 and b == n-1:
                    print('('+str(a)+','+str(b)+')')
                    break
            if a == 0 and b == n-1:
                    break
            a,b = up(a,b)
            for _ in range(n-2):
                a,b = left(a,b)
            a,b = up(a,b)
        
