# Donald and Mike are the leaders of the free world and haven’t yet (after half a year) managed to start a nuclear war. It is so great! It is so tremendous!

# Despite the great and best success of Donald’s Administration, there are still a few things he likes to complain about.

# The Mexican government is much smarter, much sharper, and much more cunning. And they send all these bad hombres over because they don’t want to pay for them. They don’t want to take care of them.

# Donald J. Trump, First Republican Presidential Debate, August 6, 2015

# He also frequently compares Mexicans to other bad people (like Germans, since they are exporting so many expensive cars to the US). Due to the tremendous amount of statements he has made (mostly containing less than 140 characters ...) the “Fake-News” New York Telegraph (NYT) has to put in a lot of effort to clarify and comment on all the statements of Donald. To check a statement, they have a list of facts they deem to be true and classify Donald’s statements into three groups: real facts (which are logical conclusions from their list of true facts), exaggerations (which do not follow, but are still consistent with the papers list of facts), and alternative facts (which contradict the knowledge of the newspaper).

# They have asked you to write a program helping them to classify all of Donald’s statements – after all it is hard for a journalist to go through them all and check them all, right?

import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())

dic = {}

for i in range(n):
    x,y = sys.stdin.readline().rstrip().split(' are worse than ')
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]

qu = deque()
for i in range(m):
    qu.clear()
    x,y = sys.stdin.readline().rstrip().split(' are worse than ')
    qu.append(x)
    check = 0
    while qu:
        t = qu.popleft()
        if t in dic:
            for i in dic[t]:
                qu.append(i)
                if i == y:
                    check = 1
                    break
            if check == 1:
                break
        else:
            continue
    if check == 1:
        print('Fact')
        continue
    
    qu.append(y)
    check = 0
    
    while qu:
        t = qu.popleft()
        if t in dic:
            for i in dic[t]:
                qu.append(i)
                if i == x:
                    check = 1
                    break
            if check == 1:
                break
        else:
            continue
    if check == 1:
        print('Alternative Fact')
        continue
    else:
        print('Pants on Fire')