# Like many families with small children, my family’s refrigerator is adorned with a set of alphabet magnets:  26 separate magnets, each containing one letter of the alphabet. These magnets can be rearranged to create words and phrases. I feel it is my parental duty to use these magnets to create messages that are witty and insightful, yet at the same time caring and supportive. Unfortunately, I am somewhat hindered in this task by the fact that I can only make phrases that use each letter once.

# For example, a nice inspiring message to leave for the children might be, “I LOVE YOU.” Unfortunately, I cannot make this message using my magnets because it requires two letter "O"s. I can, however, make the message, “I LOVE MUSTARD.” Admittedly this message isn't as meaningful, but it does manage to not use any letters more than once.

# You are to write a program that will look at a list of possible phrases and report which phrases can be written using refrigerator magnets.

# Each line will be 60 characters or less, and will consist of one or more words separated by a single space each, with words using only uppercase letters (A–Z). There will not be any leading or trailing whitespace, and there will not be any blank lines.


import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == 'END':
        break
    di = {}
    check = 0
    for i in n:
        if i != ' ':
            if i in di:
                check = 1
                break
            else:
                di[i] = 0
    if check == 0:
        print(n)