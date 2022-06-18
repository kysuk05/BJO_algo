# 19x19크기의 바둑판에, 돌을 놓을 좌표가 주어지면 이 게임이 몇 수만에 끝나는 지를 알아보려고 한다. 사용하고자 하는 바둑판의 모양은 위의 그림과 같으며, (1, 1)이 가장 왼쪽 위의 좌표이고 (19, 19)가 가장 오른쪽 아래의 좌표이다. 오목은 흑 또는 백이 5개의 돌을 가로, 세로, 혹은 대각선으로 연속으로 놓았을 경우 게임이 끝나게 된다. 즉, 다음 그림과 같은 경우를 말한다.



# 게임은 흑이 먼저 시작하며, 한수씩 서로 번갈아 가며 두게 된다. 다음 좌표들과 같이 차례로 돌을 놓으며 게임을 진행한다고 하자. (홀수번째는 흑, 짝수번째는 백)
# 위의 순서대로 바둑판에 돌을 놓으면 아래의 왼쪽 그림과 같이 된다.



# 그런데 생각해보면, 위의 좌표대로 돌을 놓았을 때 오른쪽 그림처럼 18번째의 돌을 놓는 것으로서 게임이 끝나 버리는 것을 알 수 있다. 이 경우, 답은 18이다.

# 바둑판에 돌을 놓는 좌표가 입력될 때, 몇 번째 수에서 오목이 끝나는지를 찾는 프로그램을 작성하시오. 오목을 두다 보면 다음과 같이 돌이 5개를 거치지 않고 6개 이상의 돌이 나란히 놓이는 경우가 발생할 수 있다. 이런 경우에는 승리를 인정하지 않고 오목이 계속된다는 것에 주의하라.



import sys


graph = [[0 for i in range(20)]for i in range(20)]


n = int(sys.stdin.readline())

ans = -1
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    
    if i%2 == 0:
        graph[x][y] = 1
    else:
        graph[x][y] = 2
    
    
    for j in range(4):
        cnt = 1
        if j == 0:
            temp = x
            while True:
                temp +=1
                if temp >= 20 or graph[temp][y] != graph[x][y]:
                    break
                cnt += 1
            temp = x
            while True:
                temp -=1
                if temp < 0 or graph[temp][y] != graph[x][y]:
                    break
                cnt += 1
            if cnt == 5:
                ans = i
                break
        elif j == 1:
            temp = y
            while True:
                temp +=1
                if temp >= 20 or graph[x][temp] != graph[x][y]:
                    break
                cnt += 1
            temp = y
            while True:
                temp -=1
                if temp < 0 or graph[x][temp] != graph[x][y]:
                    break
                cnt += 1
            if cnt == 5:
                ans = i
                break
        
        elif j == 2:
            temp1 = x
            temp2 = y
            while True:
                temp1 += 1
                temp2 += 1
                if temp1 >= 20 or temp2 >= 20 or graph[temp1][temp2] != graph[x][y]:
                    break
                cnt += 1
            temp1 = x
            temp2 = y
            while True:
                temp1 -=1
                temp2 -=1
                if temp1 < 0 or temp2 < 0 or graph[temp1][temp2] != graph[x][y]:
                    break
                cnt += 1
            if cnt == 5:
                ans = i
                break
        
        else:
            
            temp1 = x
            temp2 = y
            while True:
                temp1 -= 1
                temp2 += 1
                if temp1 < 0 or temp2 >= 20 or graph[temp1][temp2] != graph[x][y]:
                    break
                cnt += 1
            temp1 = x
            temp2 = y
            while True:
                temp1 +=1
                temp2 -=1
                if temp1 >= 20 or temp2 < 0 or graph[temp1][temp2] != graph[x][y]:
                    break
                cnt += 1
            if cnt == 5:
                ans = i
                break
    if ans != -1:
        break
if ans != -1:
    print(ans+1)
else:
    print(-1)