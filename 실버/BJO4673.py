#생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def d(n):
    a = n
    while n > 0:
        a += (n % 10)
        n = (n // 10)
    return a
    
a = []
for i in range(1,10001):
    a.append(i)
b = []
for i in range(1,10000):
    if (d(i) <= 10000):
        b.append(d(i))

#중복제거
b = set(b)
b = list(b)
for i in range(len(b)):
    a.remove(b[i])

for i in range(len(a)):
    print(a[i])