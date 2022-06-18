# 최근에 전기 회사는 전기 요금을 또 올렸다. 새로운 전기 요금은 아래 표에 나와있다. (사용량은 항상 양의 정수)

# 사용량 (Watt-hour)	요금 (원)
# 1 ~ 100	2
# 101 ~ 10000	3
# 10001 ~ 1000000	5
# > 1000000	7
# 위의 표를 읽는 방법은 다음과 같다.

# 사용량의 첫 100Wh의 가격은 1Wh당 2원이다. 다음 9900Wh (101 ~ 10000)의 가격은 1Wh당 3원이다. 이런식으로 계속 계산한다.

# 예를 들어, 10123Wh를 사용했을 때, 내야하는 요금은 2×100 + 3×9900 + 5×123 = 30515원이다.

# 전기 회사는 전기 요금을 인상하지 않고 돈을 더 버는 이상한 방법을 만들었다. 그 방법은 바로 사용한 전기의 양을 알려주지 않고, 얼마를 내야 하는지 알려주는 것이다. 전기 회사는 요금과 관련된 정보를 나타내는 두 숫자 A와 B를 알려준다. A와 B는 전기 회사에서 그 사람이 사는 건물에서 임의로 고른 이웃의 정보와 합친 요금이다.

# A: 이웃의 사용량과 사용량을 합쳤을 때 내야하는 요금
# B: 이웃의 전기 요금과의 차이 (절댓값)
# 위의 두 숫자를 이용해서 자신이 얼마를 내야 하는지를 계산할 수 없을 때는, 계산 요금을 100원을 더 내면 전기 회사에서 사용량을 알려준다.

# 상근이는 매우 전기를 아끼는 사람이다. 따라서, 항상 자신이 사는 건물에서 가장 전기를 적게 쓴다고 확신한다. 상근이는 돈도 전기만큼 아낀다. 따라서, 절대로 계산 요금을 지불하지 않고 자신이 직접 계산할 것이다.

# 예를 들어, A = 1100, B = 300이라고 하자. 이 정보를 이용하면, 상근이의 사용량은 150Wh, 이웃의 사용량은 250Wh임을 알 수 있다. 두 사람의 총 사용량은 400Wh이다. 따라서, A = 2×100 + 3×300 = 1100이 된다. 따라서, 상근이는 350원을 내면 된다. 상근이의 이웃은 2×100 + 3×150 = 650원을 내야 하고, B = |350 - 650| = 300이 된다.

# A와 B가 주어졌을 때, 상근이가 내야하는 전기 요금을 구하는 프로그램을 작성하시오.

import sys

while True:
    A,B = map(int,sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    if A <= 200:
        total = A//2
    elif A >200 and A <= 29900:
        total = (A-200)//3+100
    elif A>29700 and A <= 4979900:
        total = (A-29900)//5+10000
    else:
        total = (A-4979900)//7+1000000
    
    
    max_num = total//2+total%2
    min_num = 0
    
    while True:
        ans = (max_num+min_num)//2
        if max_num == min_num:
            break
        temp = ans
        money = 0
        if temp > 1000000:
            money += (temp-1000000)*7
            temp = 1000000
        if temp > 10000:
            money += (temp-10000)*5
            temp = 10000
        if temp > 100:
            money += (temp-100)*3
            temp = 100
        money += temp*2
        
        neighbor = total-ans
        temp2 = neighbor
        money2 = 0
        if temp2 > 1000000:
            money2 += (temp2-1000000)*7
            temp2 = 1000000
        if temp2 > 10000:
            money2 += (temp2-10000)*5
            temp2 = 10000
        if temp2 > 100:
            money2 += (temp2-100)*3
            temp2 = 100
        money2 += temp2*2
        
        if money2-money <= B:
            max_num = ans
        else:
            min_num = ans+1
    
    temp = ans
    money = 0
    if temp > 1000000:
        money += (temp-1000000)*7
        temp = 1000000
    if temp > 10000:
        money += (temp-10000)*5
        temp = 10000
    if temp > 100:
        money += (temp-100)*3
        temp = 100
    money += temp*2
    print(money)