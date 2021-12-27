# 줄의 개수를 세는 프로그램을 작성하시오.

# 입력
# 한 줄에 최대 100글자씩 주어진다. 빈 줄이 주어질 수도 있다.

import sys
an = 0
while True:
    s = sys.stdin.readline().rstrip()
    if s == '':
        break
    an += 1
print(an)