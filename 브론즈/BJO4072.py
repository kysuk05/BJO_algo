# A nasty virus has infected my computer. Its effect has been to attack all my text files and reverse every word in them. Your job in this problem is to write the code to restore my text files to their original condition.

# As far as the virus was concerned, a word was any sequence of characters that ended with a space or an end of line character. You will see what I mean when I tell you that the first line in one of my files was:

# Get ready for the New Zealand Programming Contest.

# The virus turned this into:

# teG ydaer rof eht weN dnalaeZ gnimmargorP .tsetnoC

# See how it included the full stop with ‘Contest’ and put it before the letters?


import sys

while True:
    li = list(map(str,sys.stdin.readline().split()))
    if li[0] == '#':
        break
    lis = []
    for i in li:
        lis.append(i[::-1])
    print(' '.join(lis))