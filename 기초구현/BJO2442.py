# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제

# 별은 가운데를 기준으로 대칭이어야 한다.

a = int(input())
for i in range(a):
    print((a-i-1)*' ' + ((i*2)+1)*('*'))