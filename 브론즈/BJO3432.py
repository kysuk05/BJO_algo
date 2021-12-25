# Tic-tac-toe is the third most popular activity to kill a lazy afternoon in Ardenia (right after solving puzzles and insulting your neighbors). Arthum and Breece are not fans of this game, but their mother told them to play, so they sit at a 5 × 5 board. Both have a large pile of marbles: marbles of Arthum have an A written on them and that of Breece have a B. However, as they are both two years old, they have no concept of rounds. Instead, they just toss their marbles as quick as possible, so after a while each board field has either marble A or marble B.

# At that point, they would like to determine the winner, but counting is not their strong point, either. (They are two years old, remember?) Recall that the goal of tic-tac-toe is to have three own marbles in a row, i.e., lying at three consecutive fields horizontally, vertically or diagonally. If both Arthum and Breece have their three marbles in a row, or neither of them has it, we call it a draw.

# The input contains several test cases. The first line of the input contains a positive integer Z ≤ 105, denoting the number of test cases. Then Z test cases follow, each conforming to the format described in section Input. For each test case, your program has to write an output conforming to the format described in section Output.


import sys
n = int(sys.stdin.readline())

for i in range(n):
    li = []
    for j in range(5):
        lis = []
        t = sys.stdin.readline().rstrip()
        for k in t:
            lis.append(k)
        li.append(lis)
    
    an1 = 0
    an2 = 0
    for a in range(5):
        for b in range(5):
            if a+2 < 5:
                if li[a][b] == li[a+1][b] == li[a+2][b]:
                    if li[a][b] == 'A':
                        an1  = 1
                    else:
                        an2 = 1
            if b+2 < 5:
                if li[a][b] == li[a][b+1] == li[a][b+2]:
                    if li[a][b] == 'A':
                        an1 = 1
                    else:
                        an2 = 1
            if a+2 < 5 and b+2 < 5:
                if li[a][b] == li[a+1][b+1] == li[a+2][b+2]:
                    if li[a][b] == 'A':
                        an1 = 1
                    else:
                        an2 = 1
            if a+2 < 5 and b-2 >= 0:
                if li[a][b] == li[a+1][b-1] == li[a+2][b-2]:
                    if li[a][b] == 'A':
                        an1 = 1
                    else:
                        an2 = 1
    if an1 == an2:
        print('draw')
    elif an1 > an2:
        print("A wins")
    elif an1 < an2:
        print("B wins")