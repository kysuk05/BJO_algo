# 2009년 날짜가 주어졌을 때, 무슨 요일인지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 D와 M이 주어진다. M월 D일이다.

# 출력
# 2009년 M월 D일의 요일을 영어로 출력한다. 출력은 다음 중 하나이다. "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday".


b,a = map(int,input().split())
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
    ans = 'Thursday'
if k == 2:
    ans = 'Friday'
if k == 3:
    ans = 'Saturday'
if k == 4:
    ans = 'Sunday'
if k == 5:
    ans = 'Monday'
if k == 6:
    ans = 'Tuesday'
if k == 0:
    ans = 'Wednesday'
print(ans)
