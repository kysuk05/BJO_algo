#n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
#자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
import sys
a = int(sys.stdin.readline().rstrip())

b = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
c = int(sys.stdin.readline().rstrip())
ans = 0

d = int(len(b)/2)
while True:
    if b[d-1] < c/2 and b[d] >= c/2:
        break
    elif b[d] > c/2:
        d -= 1
        if d-1 < 0:
            break
    else:
        d += 1
        if d >= len(b):
            break
e = d-1
while d < len(b) and e >= 0:
    if b[e] + b[d] == c:
        ans += 1
        e-=1
        d+=1
    elif b[e] + b[d]<c:
        d+=1
    else:
        e-=1


print(ans)

# 이중for문으로 해결하려니 시간초과가 생겨서 범위를 쪼개서 하는 방법으로 구현.