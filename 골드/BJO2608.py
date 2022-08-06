# 로마 시대 때는 현재 사용하는 아라비아 숫자가 아닌 다른 방법으로 수를 표현하였다.

# 로마 숫자는 다음과 같은 7개의 기호로 이루어진다.

# 기호	I	V	X	L	C	D	M
# 값	1	5	10	50	100	500	1000
# 수를 만드는 규칙은 다음과 같다.

# 보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다. 그리고 그 값은 모든 숫자의 값을 더한 값이 된다. 예를 들어 LX = 50 + 10 = 60 이 되고, MLI = 1000 + 50 + 1 = 1051 이 된다.
# V, L, D는 한 번만 사용할 수 있고 I, X, C, M은 연속해서 세 번까지만 사용할 수 있다. 예를 들어 VV나 LXIIII 와 같은 수는 없다. 그리고 같은 숫자가 반복되면 그 값은 모든 숫자의 값을 더한 값이 된다. 예를 들어 XXX = 10 + 10 + 10 = 30 이 되고, CCLIII = 100 + 100 + 50 + 1 + 1 + 1 = 253 이 된다.
# 작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 다음과 같다. IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900 을 나타낸다. 이들 각각은 한 번씩만 사용할 수 있다. 그런데 IV 와 IX 는 같이 쓸 수 없으며 XL 과 XC, CD 와 CM 또한 같이 쓸 수 없다. 이들 외에는 작은 숫자가 큰 숫자 왼쪽 어디에도 나올 수 없다. 예를 들어 XCXC 나 CMCD, VX 나 IIX 와 같은 수는 없다. 참고로 LIX = 50 + 9 = 59, CXC = 100 + 90 = 190 이 된다.
# 모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현해야 한다. 예를 들어 60 은 LX 이지 XLXX 가 아니고, 5 는 V 이지 IVI 가 아니다.
# 아래의 예를 참고 하시오.

# DLIII = 500 + 50 + 3 = 553
# MCMXL = 1000 + 900 + 40 = 1940
# 235 = CCXXXV
# 2493 = MMCDXCIII
# 로마 숫자로 이루어진 두 수를 입력받아 그 둘을 더한 값을 아라비아 숫자와 로마 숫자로 출력하는 프로그램을 작성하시오.

roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

a = input()
b = input()

x = 0
y = 0

for i in range(len(a)-1):
    if roma[a[i]] < roma[a[i+1]]:
        x -= roma[a[i]]
    else:
        x += roma[a[i]]
x += roma[a[-1]]

for i in range(len(b)-1):
    if roma[b[i]] < roma[b[i+1]]:
        y -= roma[b[i]]
    else:
        y += roma[b[i]]
y += roma[b[-1]]


ans1 = x+y

temp = x+y
ans2 = ''

n = temp // roma['M']
temp = temp % roma['M']
ans2 += 'M'*n

n = temp // roma['C']
temp = temp % roma['C']

if n >= 5:
    if n == 9:
        ans2 += 'CM'
    else:
        ans2 += 'D'+n%5*'C'
else:
    if n == 4:
        ans2 += 'CD'
    else:
        ans2 += n*'C'

n = temp // roma['X']
temp = temp % roma['X']

if n >= 5:
    if n == 9:
        ans2 += 'XC'
    else:
        ans2 += 'L'+n%5*'X'
else:
    if n == 4:
        ans2 += 'XL'
    else:
        ans2 += n*'X'

n = temp // roma['I']
temp = temp % roma['I']

if n >= 5:
    if n == 9:
        ans2 += 'IX'
    else:
        ans2 += 'V'+n%5*'I'
else:
    if n == 4:
        ans2 += 'IV'
    else:
        ans2 += n*'I'

print(ans1)
print(ans2)