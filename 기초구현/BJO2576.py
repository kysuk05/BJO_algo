# 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수을 모두 골라 그 합을 구하고, 
# 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.

a = []
cnt = 0
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        a.append(num)

for i in range(len(a)):
    cnt += a[i]
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min(a))