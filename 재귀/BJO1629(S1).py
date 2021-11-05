# 자연수 A를 B번 곱한 수를 알고 싶다. 
# 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

a,b,c = map(int,input().split())

def pow(a,b,c):
    if(b==1): return a%c
    val = pow(a,b//2,c)
    val = (val*val)%c
    if b%2 == 0: return val
    return val * a % c

print(pow(a,b,c))


#인터넷에 찾아보니 파이썬은 pow함수를 지원한다고 한다.
#이를 사용해보자.

a,b,c = map(int,input().split())
print(pow(a,b,c))