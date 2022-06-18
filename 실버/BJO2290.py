# 지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이 모니터가 잘 안나오는 것이다. 지민이의 친한 친구인 지환이는 지민이의 새로운 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다.

# 첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)이다. n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.


s,n = map(str,input().split())

s = int(s)

num = [[0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],[0,1,0,0,0,1,0,1,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,1,0,0,0,1,0,1,0],
       [0,0,0,1,0,1,0,1,0,0,0,1,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],[0,1,0,1,0,0,0,1,0,1,0,1,0,1,0],[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1,0,0,0,1,0,1,0]]

ans = [[]for i in range(2*s+3)]
row = 0

for i in n:
    numb = num[int(i)]
    for j in range(5):
        if j in (0,2,4):
            for k in range(3):
                if k != 1:
                    ans[row].append(' ')
                else:
                    if numb[j*3+k] == 0:
                        for h in range(s):
                            ans[row].append(' ')
                    else:
                        for h in range(s):
                            ans[row].append('-')
            ans[row].append(' ')
            row += 1
            
        else:
            for t in range(s):
                for k in range(3):
                    if k == 1:
                        for h in range(s):
                            ans[row].append(' ')
                    else:
                        if numb[j*3+k] == 0:
                            ans[row].append(' ')
                        else:
                            ans[row].append('|')
                ans[row].append(' ')
                row += 1
    row = 0
for i in ans:
    for j in i:
        print(j,end='')
    print()