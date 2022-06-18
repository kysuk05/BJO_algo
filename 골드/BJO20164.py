# 호석이는 짝수랑 홀수 중에서 이니셜이 같은 홀수를 더 좋아한다. 운전을 하던 호석이는 앞차의 번호판이 홀수로 가득할 때 사랑스러움을 느낄 정도이다. 전화번호도 홀수만 있고 싶다. 그렇게 홀수 홀릭에 빠진 호석이는 가지고 있는 수 N을 일련의 연산을 거치면서, 등장하는 숫자들에서 홀수를 최대한 많이 많이 보고 싶다.

# 하나의 수가 주어졌을 때 호석이는 한 번의 연산에서 다음과 같은 순서를 거친다.

# 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적는다.
# 수가 한 자리이면 더 이상 아무것도 하지 못하고 종료한다.
# 수가 두 자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각한다.
# 수가 세 자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할하고, 3개를 더한 값을 새로운 수로 생각한다.
# 호석이는 연산이 종료된 순간에 종이에 적힌 수들을 모두 더한다. 그렇게 최종적으로 얻은 수를 최종값이라고 하자. 예를 들어, 시작하는 수가 82019 라고 하자. 그럼 아래와 같이 나누게 되면 5개의 홀수를 볼 수 있기 때문에, 최종값이 5가 된다.


import sys


min_odd = sys.maxsize
max_odd = 0

n = input()

def cut_num(n,tot):
    global min_odd
    global max_odd
    for i in n:
        if int(i)%2 == 1:
            tot += 1
    if len(n) >= 3:
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                temp_1 = n[:i+1]
                temp_2 = n[i+1:j+1]
                temp_3 = n[j+1:]
                temp = str(int(temp_1)+int(temp_2)+int(temp_3))
                cut_num(temp,tot)
    elif len(n) == 2:
        temp = str(int(n[0])+int(n[1]))
        cut_num(temp,tot)
    else:
        min_odd = min(min_odd,tot)
        max_odd = max(max_odd,tot)

cut_num(n,0)

print(min_odd,max_odd)