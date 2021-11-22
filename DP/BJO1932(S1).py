# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 삼각형의 크기는 1 이상 500 이하이다. 
# 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

import sys
n = int(sys.stdin.readline())
if n != 1:
    graph = []
    for i in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))


    ans = [graph[0],[graph[1][0]+graph[0][0],graph[1][1]+graph[0][0]]]

    for j in range(2,n):
        li = []
        for k in range(len(graph[j])):
            if k == 0:
                li.append(ans[-1][0]+graph[j][0])
            elif k == len(graph[j])-1:
                li.append(ans[-1][-1]+graph[j][-1])
            else:
                li.append(max(ans[-1][k-1]+graph[j][k],ans[-1][k]+graph[j][k]))
            
            
        ans.append(li)

    print(max(ans[-1]))
else:
    print(int(sys.stdin.readline()))