# 모든 원소가 양의 정수인 집합이 있을 때, 원소를 거꾸로 뒤집고 그 원소를 오름차순으로 정렬하는 프로그램을 작성하세요.

# 단, 원소를 뒤집었을 때 0이 앞에 선행되는 경우는 0을 생략해야합니다.

# 입력
# 첫 번째로 입력되는 건 n (1 ≤ n ≤ 106)으로 사용자가 뒤이어 입력할 원소값을 결정합니다. 
# 입력하는 줄에는 하나의 원소값 뿐만 아니라 여러 원소값도 들어갈 수 있습니다.

# 단, 입력하는 정수는 1012을 넘어선 안 됩니다.

import sys
li = list(map(str,sys.stdin.readline().split()))

k = int(li.pop(0))
if  k == len(li):
    print(li)
else:
    while k != len(li):
        n = sys.stdin.readline().split()
        for i in n:
            li.append(i)


li1 = []
for i in range(len(li)):
    li1.append(int(''.join(reversed(li[i]))))
li1.sort()

for j in range(len(li1)):
    print(li1[j])
