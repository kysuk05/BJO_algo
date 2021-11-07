# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 
# 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.

import sys

n = int(sys.stdin.readline())
x = 0
y = 0

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


ans = [0,0,0]


def rec(n,x,y):
    if n == 1:
        if graph[x][y] == -1:
            ans[-1] += 1
        elif graph[x][y] == 0:
            ans[0] += 1
        else:
            ans[1] += 1 
    else:
        g = graph[x][y]
        check = 0
        for j in range(n):
            if check == 1:
                break
            for k in range(n):
                if graph[x+j][y+k] != g:
                    check = 1
                    break
        if check == 1:
            for l in range(3):
                for m in range(3):
                    rec(n//3,x+(l*n//3),y+(m*n//3))
        else:
            if graph[x][y] == -1:
                ans[-1] += 1
            elif graph[x][y] == 0:
                ans[0] += 1
            else:
                ans[1] += 1 

rec(n,x,y)

print(ans[-1])
print(ans[0])
print(ans[1])