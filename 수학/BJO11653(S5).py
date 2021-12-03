# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.


n = int(input())
stack = []
while True:
    check = 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            stack.append(i)
            n = n//i
            check = 1
            break
    if check == 0:
        break
if n != 1:
    stack.append(n)
if stack:
    for j in range(len(stack)):
        print(stack[j])