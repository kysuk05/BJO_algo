# 정수 배열 A 와 B가 있다. A는 총 n개의 서로 다른 양의 정수를 포함하고 B는 총 m개의 서로 다른 양의 정수를 포함한다.

# A, B를 이용해서 길이가 n인 새로운 배열 C를 만들어보자.

# C[i] 는 배열 B에 있는 값 중 A[i] 에 가장 가까운 값 (절대값 차이가 가장 작은 값)으로 정의 된다. 
# 만약 이 조건을 만족하는 값들이 여럿 있는 경우, 그 중 가장 크기가 작은 값으로 정의 된다.
# 예를 들어 A = [20, 5, 14, 9] 그리고 B = [16, 8, 12] 라고 해보자.

# C[1] = 16 이다 - 왜냐하면 B[1] = 16이 A[1] = 20에 가장 가깝기 때문이다.
# C[2] = 8 이다 - 왜냐하면 B[2] = 8이 A[2] = 5에 가장 가깝기 때문이다.
# C[3] = 12 이다 - 왜냐하면 B[1] = 16 와 B[3] = 12 모두 A[3] = 14에 가장 가깝지만, B[3]의 값이 더 작기 때문이다.
# C[4] = 8이다.
# 이 예제의 경우 C = [16, 8, 12, 8]으로 정의된다.

# 두 배열 A와 B가 주어졌을 때, 새로운 배열 C를 계산하여 배열 C에 포함된 값들의 합을 구하는 프로그램을 작성하시오.

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))
    B.sort()
    ans = 0
    for i in A:
        num = i
        st = 0
        ed = b-1
        while True:
            if st >= ed:
                break
            mid = (st+ed)//2
            if B[mid] <= num:
                st = mid+1
            else:
                ed = mid
        if st != 0 and B[st] - num >= num - B[st-1]:
            ans += B[st-1]
        else:
            ans += B[st]
    print(ans)