#첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.


a = int(input())
for i in range(a):
    print((i+1)*('*')+(a-i-1)*2*(' ')+(i+1)*('*'))
for i in range(a):
    print((a-i-1)*('*')+(i+1)*2*(' ')+(a-i-1)*('*'))