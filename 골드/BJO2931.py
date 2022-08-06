# 러시아 가스를 크로아티아로 운반하기 위해 자그레브와 모스코바는 파이프라인을 디자인하고 있다. 두 사람은 실제 디자인을 하기 전에 파이프 매니아 게임을 이용해서 설계를 해보려고 한다.

# 이 게임에서 유럽은 R행 C열로 나누어져 있다. 각 칸은 비어있거나, 아래 그림과 같은 일곱가지 기본 블록으로 이루어져 있다.

						
# 블록 '|'	블록 '-'	블록 '+'	블록 '1'	블록 '2'	블록 '3'	블록 '4'
# 가스는 모스크바에서 자그레브로 흐른다. 가스는 블록을 통해 양방향으로 흐를 수 있다. '+'는 특별한 블록으로, 아래 예시처럼 두 방향 (수직, 수평)으로 흘러야 한다.



# 파이프 라인의 설계를 마친 후 두 사람은 잠시 저녁을 먹으러 갔다. 그 사이 해커가 침임해 블록 하나를 지웠다. 지운 블록은 빈 칸이 되어있다.

# 해커가 어떤 칸을 지웠고, 그 칸에는 원래 어떤 블록이 있었는지 구하는 프로그램을 작성하시오.

import sys

R,C = map(int,sys.stdin.readline().split())

graph = []

for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

ans = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == '.':
            continue
        
        if graph[i][j] == '|':
            if graph[i-1][j] == '.':
                ans.append((i,j,3))
            elif graph[i+1][j] == '.':
                ans.append((i,j,1))
        
        elif graph[i][j] == '-':
            if graph[i][j-1] == '.':
                ans.append((i,j,2))
            elif graph[i][j+1] == '.':
                ans.append((i,j,4))
        
        elif graph[i][j] == '+':
            if graph[i][j-1] == '.':
                ans.append((i,j,2))
            elif graph[i][j+1] == '.':
                ans.append((i,j,4))
            elif graph[i-1][j] == '.':
                ans.append((i,j,3))
            elif graph[i+1][j] == '.':
                ans.append((i,j,1))
        
        elif graph[i][j] == '1':
            if graph[i+1][j] == '.':
                ans.append((i,j,1))
            elif graph[i][j+1] == '.':
                ans.append((i,j,4))
        
        elif graph[i][j] == '2':
            if graph[i-1][j] == '.':
                ans.append((i,j,3))
            elif graph[i][j+1] == '.':
                ans.append((i,j,4))
        
        elif graph[i][j] == '3':
            if graph[i-1][j] == '.':
                ans.append((i,j,3))
            elif graph[i][j-1] == '.':
                ans.append((i,j,2))
        
        elif graph[i][j] == '4':
            if graph[i+1][j] == '.':
                ans.append((i,j,1))
            elif graph[i][j-1] == '.':
                ans.append((i,j,2))
            

x = 0
y = 0
loc = []

if len(ans) == 4:
    s = '+'
    for i in ans:
        x += i[0]
        y += i[1]
    x //= 4
    y //= 4
    x += 1
    y += 1


else:
    if ans[0][0] == ans[1][0]:
        s = '-'
        x = (ans[0][0]+ans[1][0])//2 + 1
        y = (ans[0][1]+ans[1][1])//2 + 1
    elif ans[0][1] == ans[1][1]:
        s = '|'
        x = (ans[0][0]+ans[1][0])//2 + 1
        y = (ans[0][1]+ans[1][1])//2 + 1
    
    else:
        loc.append(ans[0][2])
        loc.append(ans[1][2])
        loc.sort()
        
        if loc[0] == 1:
            if loc[1] == 2:
                s = '2'
                x = (ans[0][0]+ans[1][0]+1)//2 + 1
                y = (ans[0][1]+ans[1][1]-1)//2 + 1
            elif loc[1] == 4:
                s = '3'
                x = (ans[0][0]+ans[1][0]+1)//2 + 1
                y = (ans[0][1]+ans[1][1]+1)//2 + 1
        else:
            if loc[1] == 3:
                s = '1'
                x = (ans[0][0]+ans[1][0]-1)//2 + 1
                y = (ans[0][1]+ans[1][1]-1)//2 + 1
            else:
                s = '4'
                x = (ans[0][0]+ans[1][0]-1)//2 + 1
                y = (ans[0][1]+ans[1][1]+1)//2 + 1

print(x,y,s)