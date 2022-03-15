# 압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 이 Q라는 문자열이 K번 반복된다는 뜻이다. 
# 압축된 문자열이 주어졌을 때, 
# 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.


import sys
li = list(sys.stdin.readline().rstrip())


stack = []
num = 0
check = 0
ans = []
for t in li:
    if t == '(':
        stack.append('(')
    elif t == ')':
        while stack[-1] != '(':
            a = stack.pop()
            if type(a) == int:
                num += a
            else:
                num += 1
        stack.pop()
        num*=int(stack.pop())
        stack.append(num)
        num = 0
    else:
        stack.append(t)

ans = 0
while stack:
    t = stack.pop()
    if type(t) == int:
        ans += t
    else:
        ans += len(t)
print(ans)