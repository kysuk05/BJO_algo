# 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.

# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange	3	1,000
# yellow	4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet	7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000
# 예를 들어, 저항의 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.


import sys
ind = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()
num1 = ind.index(a)
num2 = ind.index(b)
num3 = 10**(ind.index(c))

print(int(str(num1)+str(num2))*num3)
