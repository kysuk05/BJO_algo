# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.


a,b = map(int,input().split())

def gcd(a,b):
    num = a % b
    if num == 0:
        return b
    else:
        return gcd(b,num)

ans1 = gcd(a,b)
print(ans1)
ans2 = (a//ans1)*b
print(ans2)