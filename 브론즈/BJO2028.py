# 어떤 자연수 N을 제곱했을 때, 그 제곱수의 맨 뒷자리에 원래의 수 N이 다시 나타나면, 우리는 그 수 N을 자기복제수라고 한다.

# 예를 들면, 5의 제곱은 52는 25이고 25의 맨 뒷자리에 원래의 수 5가 나타나므로 5는 자기복제수이다. 또 다른 예로, 76의 제곱은 5776이고 5776의 맨 뒷자리에 76이 나타나므로 76 또한 자기복제수이다.

# 자연수 N이 주어졌을 때, 그 수가 자기복제수인지 아닌지를 알아내는 프로그램을 작성하시오.


import sys

a = int(sys.stdin.readline())

for i in range(a):
    k = int(sys.stdin.readline())
    t = k**2
    le = len(str(k))
    if str(t)[-le:] == str(k):
        print('YES')
    else:
        print('NO')