# 학생 $N$명이 미술 대회에 참가하였다. 이 대회에서는 주최자 한 명과 심판 한 명이 수상자를 결정하며, 수상자 결정 방식은 다음과 같다.

# 주최자와 심판이 각자 모든 학생들의 작품에 점수를 매긴다. 두 사람 모두 점수를 매길 때 서로 다른 두 작품에 같은 점수를 주지 않는다.
# 주최자가 $M$명의 학생을 골라 특별상을 수여한다.
# 심판은 특별상을 받지 않은 학생들이 그린 작품 중 자신이 매긴 점수가 가장 높은 $K$개의 작품을 추리고, 그에 해당하는 $K$명의 학생에게 본상을 수여한다.
# 주최자는 대회에서 종류와 상관 없이 상을 받는 학생들의 작품에 대해 자신이 매긴 점수의 합이 최대가 되도록 하려고 한다. 가능한 합의 최댓값을 구하여라.

import sys
n,m,k = map(int,sys.stdin.readline().split())

score = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    
    score.append((b,a))

score.sort()

ans = 0

for i in range(k):
    a,b = score.pop()
    ans += b

score.sort(key = lambda x: x[1])

for i in range(m):
    a,b = score.pop()
    ans += b
print(ans)