# 첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
# 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 
# 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 
# 블록은 적어도 하나 주어진다.

# 출력
# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.


import sys
from copy import deepcopy
n = int(sys.stdin.readline())

graph = []
for i in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    graph.append(li)
    

def move(graph):
    for i in range(n):
        stack = []
        for j in range(n):
            if graph[i][j] != 0:
                if stack and stack[-1][1] == 0 and stack[-1][0] == graph[i][j]:
                    stack[-1][0] = graph[i][j]*2
                    stack[-1][1] = 1
                else:
                    stack.append([graph[i][j],0])
        
        if stack:
            for a in range(len(stack)):
                graph[i][a] = stack[a][0]
            for b in range(len(stack),n):
                graph[i][b] = 0
        else:
            for a in range(n):
                graph[i][a] = 0
    return graph


def rotate(graph):
    graph1 = [[0 for a in range(n)] for b in range(n)]
    for i in range(n):
        for j in range(n):
            graph1[i][j] = graph[n-j-1][i]
    return graph1


ans = []
def main(graph,a):
    if a == 0:
        for i in range(n):
            for j in range(n):
                if ans:
                    if ans[-1] < graph[i][j]:
                        ans.append(graph[i][j])
                else:
                    ans.append(graph[i][j])

    else:
        graph1 = rotate(deepcopy(graph))
        graph2 = rotate(deepcopy(graph1))
        graph3 = rotate(deepcopy(graph2))
        main(move(graph),a-1)
        main(move(graph1),a-1)
        main(move(graph2),a-1)
        main(move(graph3),a-1)


main(graph,5)

print(ans[-1])

