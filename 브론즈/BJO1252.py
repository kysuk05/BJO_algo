# 두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 개의 이진수가 빈 칸을 사이에 두고 주어진다. 각 이진수는 1 또는 0으로만 이루어져 있으며, 0으로 시작할 수도 있다. 또한 각 이진수의 길이는 80을 넘지 않는다.

# 출력
# 첫째 줄에 이진수 덧셈 결과를 출력한다. 결과가 0인 경우를 제외하고는 출력되는 이진수는 항상 1로 시작해야 한다.


x,y = map(str,input().split())

n1 = int(x,2)
n2 = int(y,2)
print(bin(n1+n2)[2:])