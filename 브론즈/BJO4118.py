# Fred likes to play the lotto. Whenever he does, he buys lots of tickets. 
# Each ticket has 6 unique numbers in the range from 1 to 49, inclusive. 
# Fred likes to “Cover all his bases.” By that, he means that he likes for each set of lottery tickets to contain every number from 1 to 49, at least once, on some ticket. 
# Write a program to help Fred see if his tickets “Cover all the bases.” 

# 입력
# The input file consists of a number of test cases. Each case starts with an integer N (1 <= N <= 100), indicating the number of tickets Fred has purchased. On the next N lines are the tickets, one per line. Each ticket will have exactly 6 integers, and all of them will be in the range from 1 to 49 inclusive. No ticket will have duplicate numbers, but the numbers on a ticket may appear in any order. The input ends with a line containing only a 0.



import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    di = {}
    for i in range(1,50):
        di[i] = 0
    for i in range(n):
        s = list(map(int,sys.stdin.readline().split()))
        for j in range(6):
            if di and s[j] in di:
                di.pop(s[j])
    if di:
        print('No')
    else:
        print('Yes')