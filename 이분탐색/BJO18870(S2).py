# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.


import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

se = set(li)

li2 = sorted(list(se))
dic = {}
for i in range(len(li2)):
    dic[li2[i]] = i

for j in range(n):
    print(dic[li[j]],end=' ')