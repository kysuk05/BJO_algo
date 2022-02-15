# 두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

# 어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

# 두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

    

ans = 0
li = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            li[i][j] = li[i-1][j-1] +1
            if li[i][j] > ans:
                ans = li[i][j]

print(ans)