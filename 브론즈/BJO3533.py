# Consider 10 Boolean variables x1, x2, x3, x4, x5, x6, x7, x8, x9, and x10. Consider all pairs and triplets of distinct variables among these ten. (There are 45 pairs and 120 triplets.) Count the number of pairs and triplets that contain at least one variable equal to 1. Set f(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) = 1 if this number is odd and f(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) = 0 if this number is even.

# Here’s an explicit formula that represents the function f(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10) correctly



# In this formula ∨ stands for logical or, and ⊕ stands for exclusive or (xor). Remember that in C++ and Java these two binary operators are denoted as “||” and “^”.

# Given the values of x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, calculate the value of f(x1, x2, . . . , x10).

from itertools import combinations
li = list(map(int,input().split()))

ans = []
lis = list(combinations(li,2))
for i in lis:
    if i[0] == 1 or i[1] == 1:
        ans.append(1)
    else:
        ans.append(0)

lis = list(combinations(li,3))
for i in lis:
    if i[0] == 1 or i[1] == 1 or i[2] == 1:
        ans.append(1)
    else:
        ans.append(0)

t = ans[0]
for i in range(1,len(ans)):
    k = ans[i]
    if k == t:
        t = 0
    else:
        t = 1
print(t)