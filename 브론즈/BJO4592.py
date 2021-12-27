# Al의 초콜릿 망고 회사는 방문자들이 2d 단지에 얼마나 많은 초콜릿 망고가 있는지 추측할 수 있는 웹 사이트를 갖고 있다. 방문자들은 1부터 99까지의 수를 추측한 후 "제출" 버튼을 누르는데, 안타깝게도 서버로부터 응답시간이 종종 길어져 방문자들이 이성을 잃은 나머지 "제출"을 연타하는 사태가 발생한다. 이게 우리가 해결해야 할 문제다.

# ACM의 직원을 도와 연타된 중복을 걸러보자.


import sys
from collections import deque

while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    s = deque(list(map(str,n.split())))
    s.popleft()
    li = []
    while s:
        t = s.popleft()
        if (not li) or (li and li[-1]) != t:
            li.append(t)
    print(' '.join(li),end=' ')
    print('$')