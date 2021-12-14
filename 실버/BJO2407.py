# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

# 출력
# nCm을 출력한다.
n,m = map(int,input().split())
su = n
for i in range(1,m):
    su *= (n-i)
for j in range(1,m+1):
    su //= j
print(su)