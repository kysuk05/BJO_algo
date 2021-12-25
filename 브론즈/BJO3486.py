# The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the ancient plays are tragedies. Therefore the dramatic advisor of ACM has decided to transfigure some tragedies into comedies. Obviously, this work is very hard because the basic sense of the play must be kept intact, although all the things change to their opposites. For example the numbers: if any number appears in the tragedy, it must be converted to its reversed form before being accepted into the comedy play.

# Reversed number is a number written in arabic numerals but the order of digits is reversed. The first digit becomes last and vice versa. For example, if the main hero had 1245 strawberries in the tragedy, he has 5421 of them now. Note that all the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21). Also note that the reversed number never has any trailing zeros.

# ACM needs to calculate with reversed numbers. Your task is to add two reversed numbers and output their reversed sum. Of course, the result is not unique because any particular number is a reversed form of several numbers (e.g. 21 could be 12, 120 or 1200 before reversing). Thus we must assume that no zeros were lost by reversing (e.g. assume that the original number was 12).



import sys

n = int(sys.stdin.readline())
for i in range(n):
    x,y = map(str,sys.stdin.readline().split())
    li1 = []
    li2 = []
    for i in x:
        li1.append(i)
    for j in y:
        li2.append(j)
    li1.reverse()
    li2.reverse()
    n1 = int(''.join(li1))
    n2 = int(''.join(li2))
    li = []
    n1 = str(n1+n2)
    for i in n1:
        li.append(i)
    li.reverse()
    print(int(''.join(li)))