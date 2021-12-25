# 상근이는 체스판을 만들려고 한다.

# 체스판은 검정칸과 흰칸으로 이루어져 있다. 가장 왼쪽 위칸의 색은 검정색이고, 나머지 색은 검정과 흰색이 번갈아가면서 등장한다. 검정색은 'X'로, 흰색은 '.'로 표시한다.

# 상근이의 체스판은 R행 * C열로 이루어져 있어야 한다. 또, 각각의 행의 높이는 문자 A개만큼 이며, 각각의 열의 너비는 문자 B개 만큼이다. 예제 출력을 보고 이해하면 쉽다.

# R, C, A, B가 주어졌을 때, 상근이의 체스판을 출력하는 프로그램을 작성하시오.


R,C = map(int,input().split())

A,B = map(int,input().split())

graph = [['.'for i in range(C*B)]for j in range(R*A)]

for i in range(R*A):
    for j in range(C*B):
        if (i//A + j//B)%2 == 0:
            graph[i][j] = 'X'


for a in range(R*A):
    print(''.join(graph[a]))