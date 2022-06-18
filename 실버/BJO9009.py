# 피보나치 수 ƒK는 ƒK = ƒK-1 + ƒK-2로 정의되며 초기값은 ƒ0 = 0과 ƒ1 = 1 이다. 양의 정수는 하나 혹은 그 이상의 서로 다른 피보나치 수들의 합으로 나타낼 수 있다는 사실은 잘 알려져 있다. 

# 하나의 양의 정수에 대한 피보나치 수들의 합은 여러 가지 형태가 있다. 예를 들어 정수 100은 ƒ4 + ƒ6 + ƒ11 = 3 + 8 + 89 또는 ƒ1 + ƒ3 + ƒ6 + ƒ11 = 1 + 2 + 8 + 89, 또는 ƒ4 + ƒ6 + ƒ9 + ƒ10 = 3 + 8 + 34 + 55 등으로 나타낼 수 있다. 이 문제는 하나의 양의 정수를 최소 개수의 서로 다른 피보나치 수들의 합으로 나타내는 것이다. 

# 하나의 양의 정수가 주어질 때, 피보나치 수들의 합이 주어진 정수와 같게 되는 최소 개수의 서로 다른 피보나치 수들을 구하라.

import sys

pibo = [0,1]

t = int(sys.stdin.readline())

for i in range(t):
    temp = int(sys.stdin.readline())
    while pibo[-1] < temp:
        pibo.append(pibo[-2]+pibo[-1])
    
    arr = []
    for j in range(len(pibo)-1,-1,-1):
        if pibo[j] <= temp:
            temp -= pibo[j]
            arr.append(pibo[j])
        if temp == 0:
            break
    print(*arr[::-1])