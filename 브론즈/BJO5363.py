# 어린 제다이들은 요다와 대화하는 법을 배워야 한다. 요다는 모든 문장에서 가장 앞 단어 두 개를 제일 마지막에 말한다.

# 어떤 문장이 주어졌을 때, 요다의 말로 바꾸는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문장의 수 N이 주어진다. 둘째 줄부터 N개의 줄에는 각 문장이 주어진다. 문장의 길이는 100글자 이내이다. 단어의 개수는 3개 이상이다.



import sys
from collections import deque


n = int(sys.stdin.readline())
for i in range(n):
    t = deque(list(map(str,sys.stdin.readline().split())))
    s = t.popleft()
    t.append(s)
    s = t.popleft()
    t.append(s)
    print(' '.join(t))