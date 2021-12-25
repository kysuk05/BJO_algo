# 해밍 거리란 두 숫자의 서로 다른 자리수의 개수이다. 두 이진수가 주어졌을 때, 해밍 거리를 계산하는 프로그램을 작성하시오.

# 입력
# 입력을 여러 개의 테스트 케이스로 이루어져 있다. 첫째 줄에는 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 두 줄로 이루어져 있다. 각 줄에는 이진수가 하나씩 주어진다. 두 이진수는 길이가 서로 같고, 100자리를 넘지 않는다.



import sys

n = int(sys.stdin.readline())

for i in range(n):
    ans = 0
    x = sys.stdin.readline().rstrip()
    y = sys.stdin.readline().rstrip()
    for j in range(len(x)):
        if x[j] != y[j]:
            ans += 1
    print('Hamming distance is '+str(ans)+'.')