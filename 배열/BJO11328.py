# 두 개의 문자열에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지 판단하라.
# 각각의 테스트 케이스에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지의 여부를 
# "Impossible"(불가능) 또는 "Possible"(가능)으로 나타내시오. (따옴표는 제외하고 출력한다.)


num = int(input())

for i in range(num):
    lis1 = []
    lis2 = []
    a,b=map(str,input().split())
    for j in a:
        lis1.append(j)
    for k in b:
        lis2.append(k)
    lis1.sort()
    lis2.sort()
    if lis1 == lis2:
        print('Possible')
    else:
        print('Impossible')