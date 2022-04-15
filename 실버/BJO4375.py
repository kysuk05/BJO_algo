# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.


while True:
    try:
        n = int(input())
        num = ''
        ans = 0
        while True:
            num += '1'
            ans +=1
            if int(num)%n == 0:
                print(ans)
                break
    except:
        break

