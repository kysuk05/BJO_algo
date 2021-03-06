# 오른쪽 그림과 같은 핸드폰 자판이 있다. 이 자판을 이용하여 어떤 영어 메시지를 치려고 할 때, 걸리는 최소 시간을 구하는 프로그램을 작성하시오.

# 단, 1번은 누를 경우에는 공백이 찍힌다고 하자. 그리고 만약에 AC라는 문자를 치려 한다면 A를 치고 난 후 일정 시간을 기다린 후 C를 치면 된다.

# 하나의 문자를 입력하려면, 버튼을 눌러야 한다. 버튼을 누르면 버튼에 쓰여 있는 문자가 입력되며, 버튼을 누를 때 마다 다음 문자로 바뀌게 된다. 예를 들어, 2를 누르면 A, 2번 누르면 B, 3번 누르면 C이다. 공백을 연속으로 누를 때는 기다릴 필요가 없다.




n,m = map(int,input().split())

di = {}
di['A'] = (1,1)
di['B'] = (1,2)
di['C'] = (1,3)
di['D'] = (2,1)
di['E'] = (2,2)
di['F'] = (2,3)
di['G'] = (3,1)
di['H'] = (3,2)
di['I'] = (3,3)
di['J'] = (4,1)
di['K'] = (4,2)
di['L'] = (4,3)
di['M'] = (5,1)
di['N'] = (5,2)
di['O'] = (5,3)
di['P'] = (6,1)
di['Q'] = (6,2)
di['R'] = (6,3)
di['S'] = (6,4)
di['T'] = (7,1)
di['U'] = (7,2)
di['V'] = (7,3)
di['W'] = (8,1)
di['X'] = (8,2)
di['Y'] = (8,3)
di['Z'] = (8,4)

t = input()
ans = 0
for i in range(len(t)):
    if t[i] == ' ':
        ans += n
    else:
        ans += di[t[i]][1]*n
        if i != 0 and t[i-1] != ' ' and di[t[i-1]][0] == di[t[i]][0]:
            ans += m
print(ans)