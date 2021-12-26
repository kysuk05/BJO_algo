# A googol written out in decimal has 101 digits. A googolplex has one plus a googol digits. That's a lot of digits!

# Given any number x0, define a sequence using the following recurrence:

# xi+1 = the number of digits in the decimal representation of xi

# Your task is to determine the smallest positive i such that xi = xi-1.

import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == 'END':
        break
    else:
        li = []
        a = 0
        while True:
            a += 1
            li.append(n)
            n = str(len(n))
            if n == li[-1]:
                break
        print(a)
        

