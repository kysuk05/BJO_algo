# 4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

# 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
# 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
# X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
# 예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 

# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
# 예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

# 여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다. 


a = input()
sta = []
sum = 0
check = True
for i in a:
    if i == '(' or i == '[':
        sta.append(i)
    elif i == ')':
        if len(sta) == 0:
            check = False
            break
        elif sta[-1] == '(':
            sta.pop()
            sta.append(2)
        else:
            while sta and sta[-1]!='(':
                if sta[-1]=='[':
                    check = False
                    break
                else:
                    sum += sta.pop()
            if sta and sta[-1] == '(':
                sta.pop()
                sta.append(sum*2)
                sum = 0
            else:
                check = False
                break
    else:
        if len(sta) == 0:
            check = False
            break
        elif sta[-1] == '[':
            sta.pop()
            sta.append(3)
        else:
            while sta and sta[-1]!='[':
                if sta[-1]=='(':
                    check = False
                    break
                else:
                    sum += sta.pop()
            if sta and sta[-1] == '[':
                sta.pop()
                sta.append(sum*3)
                sum = 0
            else:
                check = False
                break

ans = 0

while sta:
    if sta[-1] == '[' or sta[-1] == '(':
        check = False
        break
    else:
        ans += sta.pop()

if check:
    print(ans)
else:
    print(0)
