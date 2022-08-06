# 전구 100개가 10×10 정사각형 모양으로 늘어서 있다. 전구에 달린 스위치를 누르면 그 전구와 위, 아래, 왼쪽, 오른쪽에 있는 전구의 상태도 바뀐다. 
# 전구 100개의 상태가 주어지면 모든 전구를 끄기 위해 최소한으로 눌러야 하는 스위치의 개수를 출력하라


import sys

graph = []

for i in range(10):
    li = []
    temp = sys.stdin.readline().rstrip()
    for j in temp:
        if j == '#':
            li.append('0')
        else:
            li.append('1')
    graph.append(li)

cnt = 0
ans = 1000

while cnt != 1024:
    k = bin(cnt)[2:]
    
    temp = [list('0'*(10-len(k))+k)]
    t = 0
    temp.extend(item[:] for item in graph)
    for i in range(1,11):
        for j in range(10):
            if temp[i-1][j] == '1':
                temp[i-1][j] = '0'
                
                if j-1 >= 0:
                    if temp[i][j-1] == '1':
                        temp[i][j-1] = '0'
                    else:
                        temp[i][j-1] = '1'
                if j+1 < 10:
                    if temp[i][j+1] == '0':
                        temp[i][j+1] = '1'
                    else:
                        temp[i][j+1] = '0'
                if i+1 < 11:
                    if temp[i+1][j] == '0':
                        temp[i+1][j] = '1'
                    else:
                        temp[i+1][j] = '0'
                if temp[i][j] == '0':
                    temp[i][j] = '1'
                else:
                    temp[i][j] = '0'
                t += 1

    if '1' not in temp[-1]:
        ans = min(ans,t)
    cnt += 1
if ans == 1000:
    print(-1)
else:
    print(ans)