# 상근이는 근처 피자 가게에서 매일 저녁으로 피자를 배달해 먹는다. 주머니 사정이 얇아진 상근이는 이번 달부터는 "최고의 피자"를 구매하려고 한다. 최고의 피자란, 피자 가게에서 주문할 수 있는 피자 중 1원당 열량이 가장 높은 피자를 말한다. 최고의 피자는 여러 종류가 있을 수도 있다.

# 이 피자 가게는 토핑 N개에서 여러 종류를 선택해서 주문할 수 있다. 같은 종류의 토핑을 2개 이상 선택할 수는 없다. 또, 토핑을 전혀 선택하지 않을 수도 있다.

# 선택한 토핑은 도우 위에 올라간다. 도우의 가격은 A원이고, 토핑의 가격은 모두 B원이다. 피자의 가격은 도우와 토핑의 가격의 합계가 된다. 즉, 토핑을 k종류 (0 ≤ k ≤ N) 선택했다면, 피자의 가격은 A + B*k원이 된다. 피자의 열량은 도우와 토핑의 열량의 합이다.

# 도우의 가격, 토핑의 가격, 그리고 도우와 각 토핑의 열량 값이 주어졌을 때, 최고의 피자의 1원 당 열량을 구하는 프로그램을 작성하시오.



import sys

n = int(sys.stdin.readline())

a,b = map(int,sys.stdin.readline().split())

dou = int(sys.stdin.readline())

top = []
for i in range(n):
    top.append(int(sys.stdin.readline()))

top.sort()


cal = []

cal.append(dou)

while top:
    x = top.pop()
    if sum(cal)/(a+b*(len(cal)-1)) < x/b:
        cal.append(x)
    else:
        break
print(sum(cal)//(a+b*(len(cal)-1)))