# 자연수 N(1 ≤ N ≤ 250)이 주어졌을 때, 2의 -N승을 계산하는 프로그램을 작성하시오. 즉, 1/(2N)을 계산하는 것이다.

# 입력
# 첫째 줄에 N이 주어진다.


n = int(input())
t = '%.300f' % 2**(-n)
li = []
check = 0
for i in t:
    li.append(i)

while li:
    t = li.pop()
    if t != '0':
        li.append(t)
        break
print(''.join(li))