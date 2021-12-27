# Freddie the frosh has chosen to take k courses. To meet the degree requirements, he must take courses from each of several categories. Can you assure Freddie that he will graduate, based on his course selection?

# 입력
# Input consists of several test cases. For each case, the first line of input contains 1 ≤ k ≤ 100, the number of courses Freddie has chosen, and 0 ≤ m ≤ 100, the number of categories. One or more lines follow containing k 4-digit integers follow; each is the number of a course selected by Freddie. Each category is represented by a line containing 1 ≤ c ≤ 100, the number of courses in the category, 0 ≤ r ≤ c, the minimum number of courses from the category that must be taken, and the c course numbers in the category. Each course number is a 4-digit integer. The same course may fulfil several category requirements. Freddie's selections, and the course numbers in any particular category, are distinct. A line containing 0 follows the last test case.


import sys
from collections import deque
while True:
    t = sys.stdin.readline().rstrip()
    di = {}
    if t == '0':
        break
    check = 0
    n,m = map(int,t.split())
    li = list(map(str,sys.stdin.readline().split()))
    for i in li:
        di[i] = 0
    for i in range(m):
        t = deque(list(map(str,sys.stdin.readline().split())))
        x = int(t.popleft())
        y = int(t.popleft())
        while t:
            k = t.popleft()
            if k in di:
                y -= 1
            if y == 0:
                break
        if y > 0:
            check = 1
    if check == 0:
        print('yes')
    else:
        print('no')