# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
check = [0]*n
ans = []
lis = []
def ad():
    if len(lis) == n:
        su = 0
        for i in range(1,len(lis)):
            su += abs(lis[i-1]-lis[i])
        ans.append(su)
    else:
        for i in range(n):
            if check[i] == 0:
                lis.append(li[i])
                check[i] = 1
                ad()
                lis.pop()
                check[i] = 0
ad()
print(max(ans))