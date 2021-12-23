# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.

# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 

# 입력
# 5개 줄에 요원의 첩보원명이 주어진다. 첩보원명은 알파벳 대문자, 숫자 0~9, 대시 (-)로만 이루어져 있으며, 최대 10글자이다.


li = []
for i in range(5):
    n = input()
    if 'FBI' in n:
        li.append(i+1)
if li:
    for i in range(len(li)):
        print(li[i],end=' ')
else:
    print('HE GOT AWAY!')