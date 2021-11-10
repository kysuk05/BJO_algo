# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)


n = int(input())

graph = [[' 'for a in range(2*n)]for b in range(n)]


def star(n,x,y):
    if n == 3:
        graph[x][y+2] = '*'
        graph[x+1][y+1] = '*'
        graph[x+1][y+3] = '*'
        graph[x+2][y] = '*'
        graph[x+2][y+1] = '*'
        graph[x+2][y+2] = '*'
        graph[x+2][y+3] = '*'
        graph[x+2][y+4] = '*'
    else:
        n = n//2
        star(n,x+n,y)
        star(n,x,y+n)
        star(n,x+n,y+(n*2))
star(n,0,0)


for i in range(n):
    print(''.join(graph[i]))