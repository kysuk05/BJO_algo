# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

import sys
m = int(sys.stdin.readline())

s = set()

for i in range(m):
    k = sys.stdin.readline().rstrip()
    if 'ad' in k:
        a = k.split()
        s.add(int(a[1]))
        continue
    elif 're' in k:
        a = k.split()
        if int(a[1]) in s:
            s.remove(int(a[1]))
        continue
    elif 'ch' in k:
        a = k.split()
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
        continue
    elif 'to' in k:
        a = k.split()
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
        continue
    elif 'al' in k:
        s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        continue
    elif 'em' in k:
        s = set([])
        continue
    