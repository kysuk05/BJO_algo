# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

import sys

n,m = map(int,sys.stdin.readline().split())


arr_A = []
arr_B = []
for i in range(n):
    arr_A.append(list(sys.stdin.readline().rstrip()))
for i in range(n):
    arr_B.append(list(sys.stdin.readline().rstrip()))


if n < 3 or m < 3:
    if arr_A == arr_B:
        print(0)
    else:
        print(-1)

else:
    ans = 0
    for i in range(n-2):
        for j in range(m-2):
            if arr_A[i][j] != arr_B[i][j]:
                ans += 1
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        if arr_A[x][y] == '0':
                            arr_A[x][y] = '1'
                        else:
                            arr_A[x][y] = '0'
    print(arr_A,arr_B)
    if arr_A == arr_B:
        print(ans)
    else:
        print(-1)