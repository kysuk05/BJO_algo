# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

# 출력
# 첫째 줄에 정답 정사각형의 크기를 출력한다.

import sys

n,m = map(int,sys.stdin.readline().split())
li = []
for i in range(n):
    k = sys.stdin.readline().rstrip()
    lis = []
    for j in k:
        lis.append(int(j))
    li.append(lis)

ans = 1
for y in range(m):
    for x in range(n):
        cnt = 1
        while True:
            if (x+cnt >= n) or (y+cnt >= m):
                break
            if li[x+cnt][y] == li[x][y+cnt] == li[x+cnt][y+cnt] == li[x][y]:
                ans = max(ans,(cnt+1)**2)
            cnt +=1

print(ans)