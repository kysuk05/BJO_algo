# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 
# 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.


n = int(input())
num = 0
while n != 1:
    num +=1
    n = n // 3
print(num)
def star(num):
    if num == 1:
        print('*'*3)
        print('*'+' '+'*')
        print('*'*3)
    else:
        for i in range(num+1):
            print(star(num-1),end='')
        print(star(num-1)+' '+star(num-1))
        for i in range(num+1):
            print(star(num-1),end='')

star(num)