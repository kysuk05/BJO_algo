# 테트리스는 C열 필드위에서 플레이하는 유명한 게임이다. 필드의 행의 수는 무한하다. 한 번 움직일 때, 아래와 같은 일곱가지 블록 중 하나를 필드에 떨어뜨릴 수 있다.



# 블록을 떨어뜨리기 전에, 플레이어는 블록을 90, 180, 270도 회전시키거나 좌우로 움직일 수 있다. 이때, 블록이 필드를 벗어나지 않으면 된다. 블록을 필드의 바닥이나 이미 채워져있는 칸의 위에 놓여지게 된다.

# 창영이가 하고있는 테트리스는 일반적인 테트리스와 약간 규칙이 다르다. 블록이 떨어졌을 때, 블록과 블록 또는 블록과 바닥 사이에 채워져있지 않은 칸이 생기면 안 된다.

# 예를 들어, 아래와 같이 각 칸의 높이가 2, 1, 1, 1, 0, 1인 경우를 생각해보자. 블록 5번을 떨어뜨리는 방법의 수는 아래와 같이 다섯가지이다.



# 테트리스 필드의 각 칸의 높이와 떨어뜨려야 하는 블록의 번호가 주어진다. 이때, 블록을 놓는 서로 다른 방법의 수를 구하는 프로그램을 작성하시오.

import sys

C,P = map(int,sys.stdin.readline().split())

fields = list(map(int,sys.stdin.readline().split()))


ans = 0

if P == 1:
    ans += C
    for i in range(C-3):
        if fields[i] == fields[i+1] == fields[i+2] == fields[i+3]:
            ans += 1

elif P == 2:
    for i in range(C-1):
        if fields[i] == fields[i+1]:
            ans += 1

elif P == 3:
    for i in range(C-2):
        if fields[i]+1 == fields[i+1]+1 == fields[i+2]:
            ans += 1
    for i in range(C-1):
        if fields[i] == fields[i+1]+1:
            ans += 1

elif P == 4:
    for i in range(C-2):
        if fields[i] == fields[i+1]+1 == fields[i+2]+1:
            ans += 1
    for i in range(C-1):
        if fields[i]+1 == fields[i+1]:
            ans += 1

elif P == 5:
    for i in range(C-2):
        if fields[i] == fields[i+1] == fields[i+2]:
            ans += 1
    for i in range(C-1):
        if fields[i] == fields[i+1]+1:
            ans += 1
    for i in range(C-1):
        if fields[i]+1 == fields[i+1]:
            ans += 1
    for i in range(C-2):
        if fields[i] == fields[i+1]+1 == fields[i+2]:
            ans += 1

elif P == 6:
    for i in range(C-1):
        if fields[i] == fields[i+1]:
            ans += 1
    for i in range(C-1):
        if fields[i] == fields[i+1]+2:
            ans += 1
    for i in range(C-2):
        if fields[i]+1 == fields[i+1] == fields[i+2]:
            ans += 1
    for i in range(C-2):
        if fields[i] == fields[i+1] == fields[i+2]:
            ans += 1

elif P == 7:
    for i in range(C-1):
        if fields[i] == fields[i+1]:
            ans += 1
    for i in range(C-1):
        if fields[i]+2 == fields[i+1]:
            ans += 1
    for i in range(C-2):
        if fields[i] == fields[i+1] == fields[i+2]+1:
            ans += 1
    for i in range(C-2):
        if fields[i] == fields[i+1] == fields[i+2]:
            ans += 1

print(ans)