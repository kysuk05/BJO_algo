# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.


n = int(input())

if n < 5:
    print(0)
elif n < 25:
    print(n//5)
elif n < 125:
    print(n//5+n//25)
else:
    print(n//5+n//25+n//125)


