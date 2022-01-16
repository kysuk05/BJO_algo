# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.


import sys


a = sys.stdin.readline().rstrip()

ans = 0
for i in a:
    if i in ('a','e','i','o','u'):
        ans += 1
print(ans)