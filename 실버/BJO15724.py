# 네모 왕국의 왕인 진경대왕은 왕국의 영토를 편하게 통치하기 위해서 1X1의 단위 구역을 여러 개 묶어서 하나의 거대 행정구역인 주지수(州地數, 마을의 땅을 셈)를 만들 예정이다. 진경대왕은 주지수를 만들기 위해서 일정한 직사각형 범위 내에 살고 있는 사람 수를 참고 자료로 쓰고 싶어한다.



# 진경대왕은 굉장히 근엄한 왕이기 때문에 당신에게 4개의 숫자로 직사각형 범위를 알려줄 것이다.

# 예를 들어, 위와 같이 사람이 살고 있다고 가정할 때 <그림 1>의 직사각형 범위의 사람 수를 알고 싶다면 진경대왕은 네 개의 정수 1 1 3 2를 부를 것이다. 마찬가지로 <그림 2>는 1 1 1 4, <그림 3>은 1 1 4 4가 될 것이다.

# 진경대왕을 위하여 이 참고 자료를 만들어내는 프로그램을 작성해보자.



import sys
n,m = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(m)]for _ in range(n)]
li = []
for a in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if (i == 0) and (j == 0):
            graph[i][j] = li[i][j]
        elif i == 0:
            graph[i][j] = graph[i][j-1] + li[i][j]
        elif j == 0:
            graph[i][j] = graph[i-1][j] + li[i][j]
        else:
            graph[i][j] = graph[i-1][j] + graph[i][j-1] + li[i][j] - graph[i-1][j-1]


t = int(sys.stdin.readline())  
for k in range(t):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x1 -=1
    y1 -=1
    x2 -=1
    y2 -=1
    if (x1 == 0) and (y1 == 0):
        print(graph[x2][y2])
    elif x1 == 0:
        print(graph[x2][y2]-graph[x2][y1-1])
    elif y1 == 0:
        print(graph[x2][y2]-graph[x1-1][y2])
    else:
        print(graph[x2][y2]-graph[x1-1][y2]-graph[x2][y1-1]+graph[x1-1][y1-1])