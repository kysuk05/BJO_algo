# 별찍기 -9
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

a = int(input())
for i in range(a):
    print(i*(' ')+((a-i)*2-1)*('*'))
for j in range(a-1):
    print((a-j-2)*(' ')+((j+1)*2+1)*('*'))