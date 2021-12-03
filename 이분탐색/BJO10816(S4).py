# ; 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# ; 입력
# ; 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# ; 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

#이분 탐색 활용
import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

li.sort()
st = 0
en = n

t = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
ans = []
for i in range(t):
    st = 0
    en = n
    while True:
        num1 = (en+st)//2
        if st == en:
            break
        else:
            if lis[i] <= li[num1]:
                en = num1
            else:
                st = num1+1
    st = 0
    en = n
    while True:
        num2 = (en+st)//2
        if st == en:
            break
        else:
            if lis[i] >= li[num2]:
                st = num2+1
            else:
                en = num2
    ans.append(num2-num1)
for j in range(t):
    print(ans[j],end=' ')
    

#Counter 함수 활용하기

from collections import Counter

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))


t = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))

c = Counter(li)
for i in range(t):
    if lis[i] in c:
        print(c[lis[i]],end=' ')
    else:
        print(0,end=' ')