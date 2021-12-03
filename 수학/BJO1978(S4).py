# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. 
# N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.


def prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        k = 2
        check = 0
        while k <= (n//2)+1:
            if n % k == 0:
                check = 1
                break
            k += 1
        if check == 0:
            return 1
        else:
            return 0
import sys
n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
ans = 0

for i in range(n):
    t = prime(li[i])
    ans += t
print(ans)