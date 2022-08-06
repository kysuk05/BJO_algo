# 피리 부는 사나이 성우는 오늘도 피리를 분다.

# 성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다. 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

# 이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해 특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다. 하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다. 

# 성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.



import sys

n,m = map(int,sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

check = [[0 for _ in range(m)] for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        dic = {}
        if check[i][j] == 0:
            dic[(i,j)] = 0
            
            check[i][j] = 1
            x = i
            y = j
            while True:
                if graph[x][y] == 'D':
                    x += dx[0]
                    y += dy[0]
                elif graph[x][y] == 'R':
                    x += dx[1]
                    y += dy[1]
                elif graph[x][y] == 'U':
                    x += dx[2]
                    y += dy[2]
                else:
                    x += dx[3]
                    y += dy[3]
                if check[x][y] == 1:
                    if (x,y) in dic:
                        ans += 1
                    break
                else:
                    check[x][y] = 1
                    dic[(x,y)] = 0
print(ans)                    