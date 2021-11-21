# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.


import sys

n = int(sys.stdin.readline())

li = []
for i in range(n):
    k = sys.stdin.readline().rstrip()
    n = len(k)
    li.append((n,k))

li = list(set(li))
li.sort()
for i in range(len(li)):
    print(li[i][1])