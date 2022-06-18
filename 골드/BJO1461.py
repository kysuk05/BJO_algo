# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

import sys


N,M = map(int,sys.stdin.readline().split())


books = list(map(int,sys.stdin.readline().split()))

pos = []
neg = []
not_return = 0

for i in range(len(books)):
    if books[i] < 0:
        neg.append(-books[i])
    else:
        pos.append(books[i])

neg.sort()
pos.sort()

if neg and pos:
    not_return = max(pos[-1],neg[-1])
elif neg:
    not_return = neg[-1]
elif pos:
    not_return = pos[-1]


ans = 0
while neg:
    if len(neg) >= M:
        ans += neg[-1]*2
        for i in range(M):
            neg.pop()
    else:
        ans += neg[-1]*2
        break

while pos:
    if len(pos) >= M:
        ans += pos[-1]*2
        for i in range(M):
            pos.pop()
    else:
        ans += pos[-1]*2
        break

ans -= not_return
print(ans)