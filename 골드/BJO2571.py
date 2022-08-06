# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 도화지에서 검은색 직사각형을 잘라내려고 한다. 직사각형 또한 그 변이 도화지의 변과 평행하도록 잘라내어야 한다.

# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다. <그림 1>에 표시된 대로 검은색 직사각형을 잘라내면 그 넓이는 22×5=110이 된다.



# <그림 1>



# <그림 2>

# 반면 <그림 2>에 표시된 대로 검은색 직사각형을 잘라내면 그 넓이는 8×15=120이 된다.

# 검은색 색종이의 수와 각 색종이를 붙인 위치가 주어질 때 잘라낼 수 있는 검은색 직사각형의 최대 넓이를 구하는 프로그램을 작성하시오.


import sys

n = int(sys.stdin.readline())

paper = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    k = max(a,b)
    l = min(a,b)
    paper.append([k,l])

paper.sort(key = lambda x : int(x[1]))

paper.sort(key = lambda x : int(x[0]))

check = [0 for i in range(n)]


for i in range(n):
    for j in range(i):
        if paper[j][0] <= paper[i][0] and paper[j][1] <= paper[i][1]:
            check[i] = max(check[i],check[j])
    check[i] += 1
print(max(check))

