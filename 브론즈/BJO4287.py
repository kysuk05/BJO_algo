# Many ‘IQ’ tests have questions of the form: king : queen :: president : ?, where the ‘correct’ answer (in USA anyway) is ‘first lady’, which says a lot about IQ tests and western culture. Because these tests are so culture laden, psychologists at the University of Northern Southwestland have devised a similar test, based on the positional difference between the letters in the words. Thus a typical problem might be: cat : dog :: emu : ? to which the answer is ‘fah’ because to go from ‘cat’ to ‘dog’ you advance the first letter by 1, the second by 14, and the third by 13. So ‘cat’ to ‘dog’ = ‘emu’ to ‘fah’. However, these same psychologists are somewhat arithmetically challenged, so they are never quite sure that they have got the right answer. This is where you come in.

# Write a program that will read in triples of words such as the ones above and determine the fourth word according to the rules outlined. Consider that the lower case alphabet wraps around at both ends, i.e. ‘a’ succeeds ‘z’ and ‘z’ precedes ‘a’.

import sys

while True:
    k = sys.stdin.readline().split()
    if k[0] == '#':
        break
    else:
        li = []
        ans = []
        for i in range(len(k[0])):
            li.append(ord(k[1][i])-ord(k[0][i]))
        for i in range(len(k[0])):
            t = ord(k[2][i])+li[i]
            if t < 97:
                t += 26
            elif t > 122:
                t -= 26
            ans.append(chr(t))
        k.append(''.join(ans))
    print(' '.join(k))