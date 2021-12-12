# 오늘은 2007년 1월 1일 월요일이다. 
# 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
a,b = map(int,input().split())
if a == 12:
    a-=1
    b += 30
if a == 11:
    a-=1
    b += 31
if a == 10:
    a-=1
    b += 30
if a == 9:
    a-=1
    b += 31
if a == 8:
    a-=1
    b += 31
if a == 7:
    a-=1
    b += 30
if a == 6:
    a-=1
    b += 31
if a == 5:
    a-=1
    b += 30
if a == 4:
    a-=1
    b += 31
if a == 3:
    a-=1
    b += 28
if a == 2:
    a-=1
    b += 31
k = b%7
if k == 1:
    ans = 'MON'
if k == 2:
    ans = 'TUE'
if k == 3:
    ans = 'WED'
if k == 4:
    ans = 'THU'
if k == 5:
    ans = 'FRI'
if k == 6:
    ans = 'SAT'
if k == 0:
    ans = 'SUN'
print(ans)
