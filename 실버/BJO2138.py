# N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

# N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오


import sys

n = int(sys.stdin.readline())

first = list(sys.stdin.readline().rstrip())
last = list(sys.stdin.readline().rstrip())

now = first[::]
cnt1 = 0
for i in range(1,n):
    if now[i-1] != last[i-1]:
        cnt1 += 1
        if now[i-1] == '0':
            now[i-1] = '1'
        else:
            now[i-1] = '0'
        if now[i] == '0':
            now[i] = '1'
        else:
            now[i] = '0'
            
        if i != n-1: 
            if now[i+1] == '0':
                now[i+1] = '1'
            else:
                now[i+1] = '0'    

if now == last:
    print(cnt1)
else:
    cnt1 = 1
    now = first[::]
    if now[0] == '0':
        now[0] = '1'
    else:
        now[0] = '0'
    if now[1] == '0':
        now[1] = '1'
    else:
        now[1] = '0'
    
    for i in range(1,n):
        if now[i-1] != last[i-1]:
            cnt1 += 1
            if now[i-1] == '0':
                now[i-1] = '1'
            else:
                now[i-1] = '0'
            if now[i] == '0':
                now[i] = '1'
            else:
                now[i] = '0'
                
            if i != n-1: 
                if now[i+1] == '0':
                    now[i+1] = '1'
                else:
                    now[i+1] = '0'  
    
    if now == last:
        print(cnt1)
    else:
        print(-1)