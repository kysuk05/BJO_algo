# 천수는 여러 종류의 주사위를 가지고 쌓기 놀이를 하고 있다. 
# 주사위의 모양은 모두 크기가 같은 정육면체이며 각 면에는 1부터 6까지의 숫자가 하나씩 적혀있다. 
# 그러나 보통 주사위처럼 마주 보는 면에 적혀진 숫자의 합이 반드시 7이 되는 것은 아니다.

# 주사위 쌓기 놀이는 아래에서부터 1번 주사위, 2번 주사위, 3번 주사위, … 의 순서로 쌓는 것이다. 
# 쌓을 때 다음과 같은 규칙을 지켜야 한다: 서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다. 
# 다시 말해서, 1번 주사위 윗면의 숫자는 2번 주사위 아랫면의 숫자와 같고, 2번 주사위 윗면의 숫자는 3번 주사위 아랫면의 숫자와 같아야 한다. 단, 1번 주사위는 마음대로 놓을 수 있다.

# 이렇게 쌓아 놓으면 긴 사각 기둥이 된다. 이 사각 기둥에는 4개의 긴 옆면이 있다. 
# 이 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다. 
# 이렇게 하기 위하여 각 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다. 
# 한 옆면의 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.

import sys
from copy import deepcopy

n = int(sys.stdin.readline())


f_dice = list(map(int,sys.stdin.readline().split()))
case1 = [f_dice[0],f_dice[5]]
case2 = [f_dice[1],f_dice[4]]
case3 = [f_dice[2],f_dice[3]]
dices = []
for j in range(n-1):
    n_dice = list(map(int,sys.stdin.readline().split()))
    dices.append(n_dice)
ans = 0


def cal(a,b):
    total = 0
    dice = [1,2,3,4,5,6]
    dice.remove(a)
    dice.remove(b)
    mnum = max(dice)
    total += mnum
    up_num = a

    now_dices = deepcopy(dices)
    for i in range(n-1):
        t_dice = now_dices[i]
        for j in range(6):
            if up_num == t_dice[j]:
                if j == 0:
                    down_num = t_dice[5]
                elif j == 1:
                    down_num = t_dice[3]
                elif j == 2:
                    down_num = t_dice[4]
                elif j == 3:
                    down_num = t_dice[1]
                elif j == 4:
                    down_num = t_dice[2]
                else:
                    down_num = t_dice[0]
        t_dice.remove(up_num)
        t_dice.remove(down_num)
        total += max(t_dice)
        up_num = down_num
    return total


result = []
result.append(cal(f_dice[0],f_dice[5]))
result.append(cal(f_dice[5],f_dice[0]))
result.append(cal(f_dice[1],f_dice[3]))
result.append(cal(f_dice[3],f_dice[1]))
result.append(cal(f_dice[2],f_dice[4]))
result.append(cal(f_dice[4],f_dice[2]))
print(max(result))
