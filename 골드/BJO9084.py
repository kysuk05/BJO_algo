# 우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다. 이 동전들로는 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다. 
# 예를 들어, 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.

# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())

for i in range(n):
    t = sys.stdin.readline()
    coin = list(map(int,sys.stdin.readline().split()))
    total = int(sys.stdin.readline())
    
    dp = [0]*(total+1)
    
    for j in coin:
        if j <= total:
            dp[j] += 1
            for k in range(j,total+1):
                dp[k] = dp[k]+dp[k-j]
    print(dp[-1])