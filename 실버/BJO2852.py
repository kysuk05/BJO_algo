# 동혁이는 NBA 농구 경기를 즐겨 본다. 동혁이는 골이 들어갈 때 마다 골이 들어간 시간과 팀을 적는 이상한 취미를 가지고 있다.

# 농구 경기는 정확히 48분동안 진행된다. 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())


x = [0,0,0]
y = [0,0,0]

ans1 = [0,0]
ans2 = [0,0]
for i in range(n):
    t,ms = sys.stdin.readline().split()
    t = int(t)
    m,s = map(int,ms.split(':'))
    
    
    if t == 1:
        if x[0] == y[0]:
            x[1] = m
            x[2] = s
            x[0] += 1
            continue
        x[0] += 1
        if x[0] == y[0]:
            x[1] = m
            x[2] = s
            ans2[0] += x[1]-y[1]
            ans2[1] += x[2]-y[2]
    
    else:
        if x[0] == y[0]:
            y[1] = m
            y[2] = s
            y[0] += 1
            continue
        y[0] += 1
        if y[0] == x[0]:
            y[1] = m
            y[2] = s
            ans1[0] += y[1]-x[1]
            ans1[1] += y[2]-x[2]


if x[0] > y[0]:
    ans1[0] += 47-x[1]
    ans1[1] += 60-x[2]
elif y[0] > x[0]:
    ans2[0] += 47-y[1]
    ans2[1] += 60-y[2]


ans1[0] += ans1[1]//60
ans1[1] %= 60

ans2[0] += ans2[1]//60
ans2[1] %= 60



if ans1[0] < 10:
    print('0'+str(ans1[0]),end='')
else:
    print(str(ans1[0]),end='')
print(':',end='')
if ans1[1] < 10:
    print('0'+str(ans1[1]))
else:
    print(str(ans1[1]))
    
if ans2[0] < 10:
    print('0'+str(ans2[0]),end='')
else:
    print(str(ans2[0]),end='')
print(':',end='')
if ans2[1] < 10:
    print('0'+str(ans2[1]))
else:
    print(str(ans2[1]))
    