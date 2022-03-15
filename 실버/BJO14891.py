# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 아래 그림과 같이 일렬로 놓여져 있다. 
# 또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 
# 톱니바퀴에는 번호가 매겨져 있는데, 가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.
# 이때, 톱니바퀴를 총 K번 회전시키려고 한다. 톱니바퀴의 회전은 한 칸을 기준으로 한다. 
# 회전은 시계 방향과 반시계 방향이 있고, 아래 그림과 같이 회전한다.
# 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다. 
# 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 
# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 
# 예를 들어, 아래와 같은 경우를 살펴보자.
# 두 톱니바퀴의 맞닿은 부분은 초록색 점선으로 묶여있는 부분이다. 
# 여기서, 3번 톱니바퀴를 반시계 방향으로 회전했다면, 4번 톱니바퀴는 시계 방향으로 회전하게 된다. 
# 2번 톱니바퀴는 맞닿은 부분이 S극으로 서로 같기 때문에, 회전하지 않게 되고, 1번 톱니바퀴는 2번이 회전하지 않았기 때문에, 회전하지 않게 된다. 
# 따라서, 아래 그림과 같은 모양을 만들게 된다.
# 위와 같은 상태에서 1번 톱니바퀴를 시계 방향으로 회전시키면, 2번 톱니바퀴가 반시계 방향으로 회전하게 되고, 2번이 회전하기 때문에, 3번도 동시에 시계 방향으로 회전하게 된다. 
# 4번은 3번이 회전하지만, 맞닿은 극이 같기 때문에 회전하지 않는다. 따라서, 아래와 같은 상태가 된다.
# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.



import sys
from collections import deque

t1 = deque(sys.stdin.readline().rstrip())
t2 = deque(sys.stdin.readline().rstrip())
t3 = deque(sys.stdin.readline().rstrip())
t4 = deque(sys.stdin.readline().rstrip())


n = int(sys.stdin.readline())


def right(t):
    x = t.pop()
    t.appendleft(x)
    return t

def left(t):
    x = t.popleft()
    t.append(x)
    return t

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a == 1:
        if t1[2] != t2[6] and t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t1 = right(t1)
                t2 = left(t2)
                t3 = right(t3)
                t4 = left(t4)
            
            elif b == -1:
                t1 = left(t1)
                t2 = right(t2)
                t3 = left(t3)
                t4 = right(t4)
        
        elif t1[2] != t2[6] and t2[2] != t3[6]:
            if b == 1:
                t1 = right(t1)
                t2 = left(t2)
                t3 = right(t3)
            elif b == -1:
                t1 = left(t1)
                t2 = right(t2)
                t3 = left(t3)
                
        elif t1[2] != t2[6]:
            if b == 1:
                t1 = right(t1)
                t2 = left(t2)
            elif b == -1:
                t1 = left(t1)
                t2 = right(t2)
            
        else:
            if b == 1:
                t1 = right(t1)
            elif b == -1:
                t1 = left(t1)
    
    elif a == 2:
        if t1[2] != t2[6] and t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t2 = right(t2)
                t1 = left(t1)
                t3 = left(t3)
                t4 = right(t4)
            elif b == -1:
                t1 = right(t1)
                t2 = left(t2)
                t3 = right(t3)
                t4 = left(t4)
        elif t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t2 = right(t2)
                t3 = left(t3)
                t4 = right(t4)
            elif b == -1:
                t2 = left(t2)
                t3 = right(t3)
                t4 = left(t4)
        elif t1[2] != t2[6] and t2[2] != t3[6]:
            if b == 1:
                t3 = left(t3)
                t2 = right(t2)
                t1 = left(t1)
            elif b == -1:
                t3 = right(t3)
                t2 = left(t2)
                t1 = right(t1)
        elif t2[2] != t3[6]:
            if b == 1:
                t2 = right(t2)
                t3 = left(t3)
            elif b == -1:
                t2 = left(t2)
                t3 = right(t3)
        elif t1[2] != t2[6]:
            if b == 1:
                t2 = right(t2)
                t1 = left(t1)
            elif b == -1:
                t2 = left(t2)
                t1 = right(t1)
        else:
            if b == 1:
                t2 = right(t2)
            elif b == -1:
                t2 = left(t2)
    
    elif a == 3:
        if t1[2] != t2[6] and t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t1 = right(t1)
                t2 = left(t2)
                t3 = right(t3)
                t4 = left(t4)
                
            elif b == -1:
                t2 = right(t2)
                t1 = left(t1)
                t3 = left(t3)
                t4 = right(t4)
        
        elif t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t3 = right(t3)
                t2 = left(t2)
                t4 = left(t4)
            else:
                t3 = left(t3)
                t2 = right(t2)
                t4 = right(t4)
        elif t1[2] != t2[6] and t2[2] != t3[6]:
            if b == 1:
                t3 = right(t3)
                t2 = left(t2)
                t1 = right(t1)
            else:
                t3 = left(t3)
                t2 = right(t2)
                t1 = left(t1)
        elif t2[2] != t3[6]:
            if b == 1:
                t3 = right(t3)
                t2 = left(t2)
            else:
                t3 = left(t3)
                t2 = right(t2)
        elif t3[2] != t4[6]:
            if b == 1:
                t3 = right(t3)
                t4 = left(t4)
            else:
                t3 = left(t3)
                t4 = right(t4)
        else:
            if b == 1:
                t3 = right(t3)
            else:
                t3 = left(t3)
        
    elif a == 4:
        if t1[2] != t2[6] and t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t4 = right(t4)
                t3 = left(t3)
                t2 = right(t2)
                t1 = left(t1)
            else:
                t4 = left(t4)
                t3 = right(t3)
                t2 = left(t2)
                t1 = right(t1)
        elif t2[2] != t3[6] and t3[2] != t4[6]:
            if b == 1:
                t4 = right(t4)
                t3 = left(t3)
                t2 = right(t2)
            else:
                t4 = left(t4)
                t3 = right(t3)
                t2 = left(t2)
        elif t3[2] != t4[6]:
            if b == 1:
                t4 = right(t4)
                t3 = left(t3)
            else:
                t4 = left(t4)
                t3 = right(t3)
        else:
            if b == 1:
                t4 = right(t4)
            else:
                t4 = left(t4)
    

total = 0
if t1[0] == '1':
    total += 1
if t2[0] == '1':
    total += 2
if t3[0] == '1':
    total += 4
if t4[0] == '1':
    total += 8
print(total)

