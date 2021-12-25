# A worm is going to eat chocolate in a form of a rectangle with M rows and N columns.

# It starts eating at the upper left corner and eats the entire row to its end. It then turns clockwise and continues to eat the whole column (the last one). Upon reaching its end, the process is repeated, i.e. the worm turns clockwise and eats the entire last row. By repeating this process of eating the chocolate, worm will eat the whole chocolate.

# Write a program that will compute the number of turns the worm made until it ate the whole chocolate.

# 입력
# The first and only line of the input contains two integers, M and N, 2 ≤ M,N ≤ 100,. separated by a space character. M is number of rows and N is number of columns. 


#1952번 달팽이2 문제랑 완전히 같은 것 같다

a,b = map(int,input().split())

if a > b:
    print(b*2-1)
else:
    print(a*2-2)