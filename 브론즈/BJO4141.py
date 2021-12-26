# Anna and Bob are starting up a new high-tech company. Of course, one of their key considerations is choosing a good name for the company. Palindromes are cool. (A palindrome is a word that is the same when reversed, like the names of our two entrepreneurs.) They would really the name of their company to be a palindrome. Unfortunately, they cannot think of a nifty company name that is also a palindrome.

# Maybe at least the telephone number of their company could be a palindrome. However, they really want their customers to be able to call them, so they want to choose the company name so that, when it is typed using the letters printed on a phone keypad, the result is also their phone number. (On a standard phone keypad, the following keys contain the corresponding letters: 2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ.)


import sys

n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    s = s.upper()
    li = []
    for j in s:
        if j in ('A','B','C'):
            li.append('2')
        elif j in ('D','E','F'):
            li.append('3')
        elif j in ('G','H','I'):
            li.append('4')
        elif j in ('J','K','L'):
            li.append('5')
        elif j in ('M','N','O'):
            li.append('6')
        elif j in ('P','Q','R','S'):
            li.append('7')
        elif j in ('T','U','V'):
            li.append('8')
        else:
            li.append('9')
    s = ''.join(li)
    k = s[::-1]
    if k == s:
        print('YES')
    else:
        print('NO')