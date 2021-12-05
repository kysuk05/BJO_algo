# 길이가 $N$인 수열 $S$가 있다. 수열 $S$는 1 이상인 정수로 이루어져 있다.

# 수열 $S$에서 원하는 위치에 있는 수를 골라 최대 $K$번 삭제를 할 수 있다.

# 예를 들어, 수열 $S$가 다음과 같이 구성되어 있다고 가정하자.

# 수열 S : 1 2 3 4 5 6 7 8
# 수열 $S$에서 4번째에 있는 4를 지운다고 하면 아래와 같다.

# 수열 S : 1 2 3 5 6 7 8 
# 수열 $S$에서 최대 $K$번 원소를 삭제한 수열에서 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 구해보자.

import sys
n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))

an = 0
num = 0
le = 0
en = 0
for i in range(n):
    while en < n and num <= m:
        if li[en] % 2 == 1:
            num += 1
        else:
            le += 1
        en += 1
    
    if le > an:
        an = le
    
    if li[i] % 2 == 1:
            num -= 1
    else:
        le -= 1
print(an)