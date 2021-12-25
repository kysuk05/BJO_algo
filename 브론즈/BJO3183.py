# Dates are often expressed as a sequence of numbers to represent the day, month and year. The 14th August 2004, for example, can be expressed as 14 8 2004. Programs that accept dates as input have to check that the numbers supplied are valid, which is what this problem is about.

# What could be wrong with a date? Well here are some obvious examples:

# 12 0 2004 : There is no month 0.
# 32 1 1976 : January has only 31 days.
# 29 2 1974 : 1974 was not a leap year so there was no 29th February.

# Hopefully you know that most months have 31 days, except for April, June, September and November which have 30, and February which has 28 (29 in a leap year). Every 4th year is a leap year, so if you can divide the year number exactly by 4 then it is a leap year. Well, that is normally correct, but at the turn of a century, where the year can be divided exactly by 100, it is not a leap year. There is one more exception though! You may remember that the year 2000 was a leap year because it can be divided exactly by 400.

while True:
    x,y,z = map(int,input().split())
    if x == 0 and y == 0 and z == 0:
        break
    if x <=0 or x > 31:
        print('Invalid')
    elif y <= 0 or y >12:
        print('Invalid')
    elif y in (4,6,9,11) and x == 31:
        print('Invalid')
    elif y == 2 and x == 30:
        print('Invalid')
    elif y == 2 and ((z % 4 != 0) or (z% 400!= 0 and z%100 == 0)) and x == 29:
        print('Invalid')
    else:
        print('Valid')