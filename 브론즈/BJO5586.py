# 입력으로 주어지는 문자열에서 연속으로 3개의 문자가 JOI 또는 IOI인 곳이 각각 몇 개 있는지 구하는 프로그램을 작성하시오. 문자열은 알파벳 대문자로만 이루어져 있다. 예를 들어, 아래와 같이 "JOIOIOI"에는 JOI가 1개, IOI가 2개 있다.



import sys

s = sys.stdin.readline().rstrip()
joi = 0
ioi = 0
for i in range(len(s)):
    if i > 1 and s[i] == 'I':
        if s[i-1] == 'O' and s[i-2] == 'J':
            joi += 1
        elif s[i-1] == 'O' and s[i-2] == 'I':
            ioi += 1
print(joi)
print(ioi)