#알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
#단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

a = input()
a = a.upper()

lis1 = []
for i in a:
    lis1.append(i)

set1 = set(lis1)

#스택과 집합을 이용해서 풀기
sta = []
max = 0
for j in set1:
    if max <= lis1.count(j):
        sta.append(j)
        max = lis1.count(j)

if len(sta)>=2 and lis1.count(sta[-1]) == lis1.count(sta[-2]):
    print('?')
else:
    print(sta[-1])