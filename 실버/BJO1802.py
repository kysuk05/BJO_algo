# 동호는 종이를 접는데 옆에서 보고 접으려고 한다. 옆에서 본다는 말은 아래 그림과 같이 본다는 뜻이다. 동호는 종이를 반으로 접을 때, 아래와 같이 두가지중 하나로만 접을 수 있다.

# 오른쪽 반을 반시계 방향으로 접어서 왼쪽 반의 위로 접는다.
# 오른쪽 반을 시계 방향으로 접어서 왼쪽 반의 아래로 접는다.
# 아래의 그림은 위의 설명을 그림으로 옮긴 것이다.



# 한 번의 종이 접기가 끝났을 때, 동호는 종이 접기를 원하는 만큼 더 할 수 있다. 종이 접기를 한번 접을 때 마다 두께는 2배가 되고 길이는 절반이 될 것이다.



# 종이 접기를 여러 번 했을 때 (안접을 수도 있다), 동호는 종이를 다시 피기로 했다. 그러고 나서 다시 접고 이렇게 놀고 있었다. 옆에서 보고 있던 원룡이는 동호를 위해 종이를 접어서 주기로 했다.(원룡이는 동호의 규칙대로 접지 않는다.) 동호는 그리고 나서 원룡이가 접었다 핀 종이를 다시 동호의 규칙대로 접을 수 있는지 궁금해졌다.

# 위의 저 종이를 접었다 피면 다음과 같은 그림처럼 펴진다.



# 종이가 시계방향으로 꺽여있으면 OUT이고, 반시계방향으로 꺾여있으면 IN이다.

# 종이가 접혀있는 정보가 왼쪽부터 오른쪽까지 차례대로 주어졌을 때, 이 종이를 동호의 규칙대로 접을 수 있는지 없는지를 구하는 프로그램을 작성하시오.


import sys
from collections import deque

n = int(sys.stdin.readline())


for i in range(n):
    temp = sys.stdin.readline().rstrip()
    qu = deque()
    ans = 'YES'
    
    
    qu.append(temp)
    while qu:
        temp = qu.popleft()
        if len(temp) == 1:
            break
        ind = len(temp)//2
        
        a = temp[:ind]
        b = temp[ind+1:]
        for i in range(len(a)):
            if a[i] == b[len(a)-i-1]:
                ans = 'NO'
                break
        if ans == 'NO':
            break
        qu.append(a)
        qu.append(b)
    print(ans)